from django.shortcuts import render
from .forms import EventForm
from django.shortcuts import render
from web3 import Web3
import json
from django.core.serializers import serialize
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def dashboard(request):
    return render(request,"dashboard.html")
def host(request):
    return render(request,"host.html")
def book(request):
    return render(request,"book.html")
def about(request):
    return render(request,"about.html")
def booking(request):
    return render(request,"booking.html")





def index(request):
    events = []
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.cleaned_data
            events.append(event)
    else:
        form = EventForm()
    
    return render(request, 'index.html', {'form': form, 'events': events})




w3 = Web3(Web3.HTTPProvider(
    'https://evm.ngd.network:32332'))




def save_blog(request):
    ids = ['#title', '#description', '#content', '#Category', '#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    # set the contract address and ABI
    contract_address = '0xb07d0Af83889b79515009dD130eF7c14EEeF9a5B'
    my_address= "9df0f165de14ab2729bd5fcdb58dfbb3ec6131efc979068da4548d4ef2cb8b9a"
    contract_abi = json.loads([
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_eventId",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_numTickets",
				"type": "uint256"
			},
			{
				"internalType": "address payable",
				"name": "_destinationWallet",
				"type": "address"
			}
		],
		"name": "buyTicket",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_location",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_date",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_totalTickets",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_ticketPrice",
				"type": "uint256"
			}
		],
		"name": "createEvent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": "false",
		"inputs": [
			{
				"indexed": "true",
				"internalType": "uint256",
				"name": "eventId",
				"type": "uint256"
			},
			{
				"indexed": "true",
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": "false",
				"internalType": "uint256",
				"name": "remainingTickets",
				"type": "uint256"
			}
		],
		"name": "TicketPurchased",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "events",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "date",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "totalTickets",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "ticketPrice",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAllEventDetails",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "names",
				"type": "string[]"
			},
			{
				"internalType": "string[]",
				"name": "locations",
				"type": "string[]"
			},
			{
				"internalType": "uint256[]",
				"name": "dates",
				"type": "uint256[]"
			},
			{
				"internalType": "uint256[]",
				"name": "times",
				"type": "uint256[]"
			},
			{
				"internalType": "uint256[]",
				"name": "totalTickets",
				"type": "uint256[]"
			},
			{
				"internalType": "uint256[]",
				"name": "ticketPrices",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getEventCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_eventId",
				"type": "uint256"
			}
		],
		"name": "getEventDetails",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "date",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "totalTickets",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "ticketPrice",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
])
    # create an instance of the contract
    simple_storage = w3.eth.contract(
        address=contract_address, abi=contract_abi)
    nonce = w3.eth.get_transaction_count(my_address)

    print("transaction sucess..")

    greeting_transaction = simple_storage.functions.createBlogPost(
        str(title), str(description), str(
            content), str(Thumbnail), str(Category)
    ).build_transaction(
        {
            "chainId": w3.eth.chain_id,
            'gas': 700000,
            'gasPrice': w3.eth.gas_price,
            "from": my_address,
            "nonce": nonce,
        }
    )

    # Wait for the transaction to be mined
    signed_txn = w3.eth.account.sign_transaction(
        greeting_transaction, private_key=my_address)

    # send the signed transaction to the network    
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # get the transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt.get('transactionHash'))
    if tx_receipt.blockNumber:
        print("Transaction hash code : ", tx_receipt,
              'Block number : ', tx_receipt.blockNumber)

        # obj = Blog(title=title, description=description, content=content,
        #            categories=Category, blog_profile_img=Thumbnail, Block_chin_blockNo=tx_receipt.blockNumber, trans_detial=tx_receipt)
        # obj.save()

    return JsonResponse({"result": (json.loads(serialize('json', ["page"])))[0]})
