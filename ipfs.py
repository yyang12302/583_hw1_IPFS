import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data=json.dumps(data)
	files={
		'file':('data.json',json_data,'application/json')
	}

	gateway="https://api.pinata.cloud/pinning/pinFileToIPFS"
	headers={
		'pinata_api_key':'6bf509970b4e9c3ecee6',
		'pinata_secret_api_key':'d935f96f288a65d6fd2b5984af63efa47d6022cc03cba8aeebefd65a330fa9a6'

	}
	response = requests.post(gateway, files=files, headers=headers)
	cid = response.json()['IpfsHash']


	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	gateway="https://api.pinata.cloud/pinning/pinFileToIPFS"
	headers={
		'pinata_api_key':'6bf509970b4e9c3ecee6',
		'pinata_secret_api_key':'d935f96f288a65d6fd2b5984af63efa47d6022cc03cba8aeebefd65a330fa9a6'

	}
	response = requests.get(gateway, headers=headers)
	print(response.json())
	if content_type =="json":
		data = response.json()
	else:
		data = response.content

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
