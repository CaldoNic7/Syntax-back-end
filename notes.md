# Django New Resource General Steps
1. Create a new model file & class
2. Create one or more serializers for your model
3. Create a views file & a view class/method
4. Add a URL path to the urls.py file
5. Generate & run migrations
6. Test!


# Django CRUD View Steps
1. Query the data (one or multiple mangos) or prepare new data like for create
2. Serialize the data (format it, create new data, update an existing object) and Validate/save data if necessary
3. Return response to the client w/ data or errors
