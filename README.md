![Python](https://img.shields.io/badge/python-v3.6-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Pypi version](https://img.shields.io/badge/pypi-0.0.4-ff69b4)

# Kitaab

### Create beautiful notes right from the terminal

<img width="908" alt="Screenshot 2022-06-18 at 1 11 32 AM" src="https://user-images.githubusercontent.com/90202062/174393139-8d843851-03ad-4596-a1b6-709364f4bec7.png">

### Publish your notes to Github


https://user-images.githubusercontent.com/90202062/181063195-b5cf53d5-f8cf-497e-8722-b3a7e586b594.mov


## Install
```
pip install kitaab
```
## Run
```
python -m kitaab
```
## Usage
```
help
```
<img width="629" alt="Screenshot 2022-06-18 at 1 21 13 AM" src="https://user-images.githubusercontent.com/90202062/174393010-55f6dd56-bdc9-46ac-ae93-7500998efec6.png">

```
board
```
<img width="1347" alt="Screenshot 2022-06-18 at 1 22 01 AM" src="https://user-images.githubusercontent.com/90202062/174393613-96fdd76b-dd8d-4bd7-9e72-a4dff71abf3f.png">

## Generate token to publish notes to Github repository [OPTIONAL]
You can skip this if you don't want to publish your notes to github repository. Your notes will be safe in local sqlite3 database<br/>
Uploading notes to github requires Authentication. Thankfully, Github users can generate Tokens to access GithubApi.

You can easily generate one for yourself by following the steps below:
1. Sign in to your Github account
2. Go to `settings`
3. Navigate to `Developer settings`
4. Click on `Personal access tokens`
5. Click on `Generate new Token`
6. Give it a name , set expiration date and `click on repo` under scopes
7. Navigate down and click on green button `Generate token`
8. Make sure to `copy your personal access token` now, you won't be able to see it again. 
  <p align="center">
  <img width="807" alt="Screenshot 2022-06-18 at 1 46 30 AM" src="https://user-images.githubusercontent.com/90202062/174395618-e81209a6-7749-4c9d-8bed-a6b12792b6e8.png">
  </p>


## How to add token
```
add-token
```
<img width="508" alt="Screenshot 2022-06-18 at 2 13 21 AM" src="https://user-images.githubusercontent.com/90202062/174398731-5e9214a2-a823-4ef5-b500-1e4d32025cfb.png">


