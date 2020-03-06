import requests
# url="http://127.0.0.1:8000/api/users_list/"
# response=requests.get(url)
# print(response.text)

URL="http://127.0.0.1:8000"

def get_token():
	# Get Auth Token
	url=f"{URL}/api/auth"
	response=requests.post(url,data={'username':"paul1","password":"paul1"})
	return (response.json())
get_token()


def get_data():
	url=f"{URL}/api/users_list/"
	token=get_token()
	header={"Authorization":f"Token {get_token()} "}
	#print (f"Token {get_token()}")
	response=requests.get(url,headers=header)
	emp_data=response.json()
	return emp_data


def create_new():
	url=f"{URL}/api/users_list/"
	token=get_token()
	header={"Authorization":f"Token {get_token()} "}
	data={
		"id": 1,
       	"employee_id": "hq006",
        "name": "Ajakaye Paul",
        "age": 28,
        "ranking": 1.0

	}
	#print (f"Token {get_token()}")
	response=requests.post(url,data=data,headers=header)
	emp_data=response.json()
	print(emp_data)





def edit_data(employee_id):
	url=f"{URL}/api/users_list/{employee_id}/"
	token=get_token()
	header={"Authorization":f"Token {get_token()} "}
	data=	{
	    "employee_id": "hq001",
	    "name": "Ajakaye Paul Adeniran Festus Adebimpe",
        "age": 22,
        "ranking": 1.0

	}
	#print (f"Token {get_token()}")
	response=requests.put(url,data=data,headers=header)
	emp_data=response.text
	print(emp_data,response.status_code)

#create_new()
edit_data(1)

