# ImageRepo

## Setup

### Virtual Environment
Follow instructions from
https://docs.python.org/3/tutorial/venv.html
to set up virtual environment with requirements.txt. 

### Run server locally
Navigate to the `imagerepo` folder in the project root. 

Run the following commands: 
`python3 ./manage.py makemigrations`
`python3 ./manage.py migrate`
`python3 manage.py runserver`

Then navigate to http://127.0.0.1:8000/ to view project. 

## How to use the application
The homepage is where you can view all the photos you have uploaded in a grid like view.

To upload a picture, click on "Upload" at the top navigation bar.
Add a title for your image, a tag (to filter searches by) and choose your image.
You will see a confirmation message once your image has been uploaded.

Navigate back to the homepage by clicking on the "Imagery" text. 
See your newly uploaded image added to the grid.

## Next Steps
This application covers the foundation of an image repo. 
The feature to search by tag or title has not yet been implemented.
A great next step would be to implement this feature. 

The user interface can definitely be improved. 

In addition: 
- option to upload multiple files
- view images by recently uploaded/oldest uploads
- ability to favourite images
- ability to delete images
