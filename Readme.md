#Appointment Scheduler

Simple API to schedule users appointments


##Content
1. [Requirements](#Requirements)
2. [Installation](#Installation)
   1. [Using Linux](#Using Linux or WSL in MS Windows) 
   2. [Using Docker](#Using Docker)
3. [Usage](#Usage)
4. [API Doc](#API)

### Requirements
Python (> 3.6)

Python virtualenv (Optional)

Docker (Only for docker installation)
***

###Installation

####Using Linux or WSL in MS Windows
Clone the repository
```
git clone https://github.com/ferjflores/scheduler_api.git
cd scheduler_api
```
Create a virtual environment (Optional)
```
virtualenv -ppython3 .venv
source .venv/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```
To start the API
```
python run.py
```
After that the API should be running on http://localhost:5000


####Using Docker
```
docker pull ferjflores/scheduler_api
```
Run the docker image
```
docker run -d -p 5000:5000 -t ferjflores/scheduler_api
```
After that the API should be running on http://localhost:5000

***

###Usage

####Create and appointment
curl --request POST \
  --url http://localhost:5000/api/appointment/ \
  --header 'Content-Type: application/json' \
  --data '{
	"user_id": "test_user_id",
	"requested_date": "20211116083000"
}'

####Get all appointments for the user
curl --request GET \
  --url http://localhost:5000/api/user/test_user_id

***

###API 

**Add Appointment**
```
POST /api/appointment/
```
Parameters:

|Name | Type | Mandatory | Description |
|----|----|-----|----|
|user_id  | String | Yes | Any string is a valid user_id |
|requested_date | String | Yes | Any valid format date time |

Response:
```
{
  "date": "2021-11-16",
  "time": "08:30",
  "user_id": "user_id"
}
```

**List user Appointments**
```
POST /api/appointments/{user_id}
```
Parameters:

|Name | Type | Mandatory | Description |
|----|----|-----|----|
|user_id  | String | Yes | A valid user_id |

Response:

```
[
  {
    "date": "2021-11-16",
    "time": "08:30"
  },
  {
    "date": "2021-11-15",
    "time": "09:30"
  },
  {
    "date": "2021-11-05",
    "time": "11:00"
  }
]
``


