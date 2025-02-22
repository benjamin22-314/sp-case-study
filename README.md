## Case Study

### Task 1
My answer to the puzzle.

### Task 2
An app that allows the user to upload an image of a ID (from one of ten countries), and receive the probabilities of which country the ID is for.

Here are the instructions for running the different parts.

##### Model training

Data - put images into the `model_training/images` directory. The images should be grouped into folders by label.

Virtual Environment - in the `model_training` directory. These instructions are for windows, MacOS/Linux will be a little different.
- create the venv; `python3 -m venv <environment_name>`
- activate the venv; `<environment_name>\Scripts\activate`
- install the requirements; `pip install -r requirements.txt`
- create ipykernal; `python -m ipykernel install --user --name=<environment_name>`
- open `training.ipynb`, select the venv as the kernel, and run the cells.

Have a look at the training notebook to view the model evaluation.

##### Running the App
You need to have docker compose installed and running on your computer. In powershell/command line/bash run `docker-compose up --build`. Go to you browser and open `http://localhost/`. You will there see a UI that will allow you to upload an image of an ID and receive predictions about which country (of the countries listed below) the ID is from;

• alb_id (ID Card of Albania)
• aze_passport (Passport of Azerbaijan)
• esp_id (ID Card of Spain)
• est_id (ID Card of Estonia)
• fin_id (ID Card of Finland)
• grc_passport (Passport of Greece)
• lva_passport (Passport of Latvia)
• rus_internalpassport (Internal passport of Russia)
• srb_passport (Passport of Serbia)
• svk_id (ID Card of Slovakia)

![Screenshot of UI](/screenshots/ui_screenshot.png)

##### Potential Improvements

Model training;
- Use more data. Use augmented data.
- Try OpenCV/YOLO to crop the ID out of the image.
- Different model architectures (e.g. Conv3d instead of Conv2d, more layers, regularisation, allow any size input).
- Make "category" to "label" mapping fixed. 

App;
- Remove duplication of model class code.
- Add more error handling.
- Add tests.
- Build a nicer UI (e.g. use React).
- use a paid API (e.g. an OpenAI LLM, Amazon Textract, ect) instead of our own model.