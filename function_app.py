import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def get_user_info(name, surname, id_number):
    while True:
        id_number = input("Enter your ID number: ")

        if len(id_number) == 9:
            return f"Data entered is correct. Name: {name}, Surname: {surname}, ID Number: {id_number}"
        else:
            print("ID number is incorrect. It must contain 9 characters. Please try again.")

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #for GET I think
    name = req.params.get('name')
    surname = req.params.get('surname')
    id_number = req.params.get('id_number')

    #If not a Get request
    if not name or not surname:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            #for POST
            name = req_body.get('name')
            surname = req_body.get('surname')
            id_number = req_body.get('id_number')


    if name and surname and len(id_number) == 9:
        return func.HttpResponse(f"Hello, {name} {surname} with id:{id_number}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "Id must contain 9 characters",
             status_code=200
        )