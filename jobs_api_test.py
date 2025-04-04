import requests

#
# resp = requests.get('http://localhost:8080/api/jobs')
# if resp.status_code == 200:
#     print("OK", resp.json())
# else:
#     print("Error", resp.status_code, resp.json()["error"])
#
# resp = requests.get('http://localhost:8080/api/jobs/2')
# if resp.status_code == 200:
#     print("OK", resp.json())
# else:
#     print("Error", resp.status_code, resp.json()["error"])
#
# resp = requests.get('http://localhost:8080/api/jobs/2222')
# if resp.status_code == 200:
#     print("OK", resp.json())
# else:
#     print("Error", resp.status_code, resp.json()["error"])
#
# resp = requests.get('http://localhost:8080/api/jobs/qwertyui')
# if resp.status_code == 200:
#     print("OK", resp.json())
# else:
#     print("Error", resp.status_code, resp.json()["error"])


resp = requests.post('http://localhost:8080/api/jobs',
                     json={
                         "job":"New Job",
                         "work_size":12,
                         "collaborators": "1",
                         "is_finished": False,
                         "team_leader": 1
                     })
if resp.status_code == 201:
    print("OK", resp.json())
else:
    print("Error", resp.status_code, resp.json()["error"])
