from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.goal import Goal
from ..serializers import GoalSerializer

# Create your views here.


class Goals(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GoalSerializer

    def get(self, request):
        """Index request"""
        # Get all the goals:
        # goals = Goal.objects.all()
        # Filter the goals by owner, so you can only see your owned goals
        goals = Goal.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = GoalSerializer(goals, many=True).data
        return Response({'goals': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['goal']['owner'] = request.user.id
        # Serialize/create goal
        goal = GoalSerializer(data=request.data['goal'])
        # If the goal data is valid according to our serializer...
        if goal.is_valid():
            # Save the created goal & send a response
            goal.save()
            return Response({'goal': goal.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(goal.errors, status=status.HTTP_400_BAD_REQUEST)


class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the goal to show
        goal = get_object_or_404(Goal, pk=pk)
        # Only want to show owned goals?
        if request.user != goal.owner:
            raise PermissionDenied('Unauthorized, this isn\'t your goal.')

        # Run the data through the serializer so it's formatted
        data = GoalSerializer(goal).data
        return Response({'goal': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate goal to delete
        goal = get_object_or_404(Goal, pk=pk)
        # Check the goal's owner against the user making this request
        if request.user != goal.owner:
            raise PermissionDenied('Unauthorized, this isn\'t your goal.')
        # Only delete if the user owns the  goal
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate goal
        # get_object_or_404 returns a object representation of our Goal
        goal = get_object_or_404(Goal, pk=pk)
        # Check the goal's owner against the user making this request
        if request.user != goal.owner:
            raise PermissionDenied('Unauthorized, this isn\'t your goal.')

        # Ensure the owner field is set to the current user's ID
        request.data['goal']['owner'] = request.user.id
        # Validate updates with serializer
        data = GoalSerializer(goal, data=request.data['goal'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
