from django.shortcuts import render
from ticket3.settings import my_address, private_key
from web3 import Web3
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")

def book(request):
    return render(request, "book.html")

def about(request):
    return render(request, "about.html")

def booking(request):
    return render(request, "booking.html")

def host(request):
    if request.method == 'POST':
        ids = ['#EventName', '#location','#date', '#time',  '#Seat', '#ticket']
        name = request.POST.get(ids[0])
        location = request.POST.get(ids[1])
        date = int(request.POST.get(ids[2]))  # Convert to int
        time = int(request.POST.get(ids[3]))  # Convert to int
        total_tickets = int(request.POST.get(ids[5]))  # Convert to int
        ticket_price = int(request.POST.get(ids[6])) # Convert to int

        w3 = Web3(Web3.HTTPProvider('https://polygon-mumbai.g.alchemy.com/v2/K59YdNGK95akCLJrA1m9nYPZ7JYNa8Me'))

        contract_address = '0xb07d0Af83889b79515009dD130eF7c14EEeF9a5B'

        contract_abi = json.loads('[ { "inputs": [ { "internalType": "uint256", "name": "_eventId", "type": "uint256" }, { "internalType": "address payable", "name": "_destinationWallet", "type": "address" }, { "internalType": "uint256", "name": "_numTickets", "type": "uint256" } ], "name": "buyTicket", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_location", "type": "string" }, { "internalType": "uint256", "name": "_date", "type": "uint256" }, { "internalType": "uint256", "name": "_time", "type": "uint256" }, { "internalType": "uint256", "name": "_totalTickets", "type": "uint256" }, { "internalType": "uint256", "name": "_ticketPrice", "type": "uint256" } ], "name": "createEvent", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "uint256", "name": "eventId", "type": "uint256" }, { "indexed": true, "internalType": "address", "name": "buyer", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "remainingTickets", "type": "uint256" } ], "name": "TicketPurchased", "type": "event" }, { "inputs": [], "name": "conversionRate", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "events", "outputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "string", "name": "location", "type": "string" }, { "internalType": "uint256", "name": "date", "type": "uint256" }, { "internalType": "uint256", "name": "time", "type": "uint256" }, { "internalType": "uint256", "name": "totalTickets", "type": "uint256" }, { "internalType": "uint256", "name": "ticketPrice", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getAllEventDetails", "outputs": [ { "internalType": "string[]", "name": "names", "type": "string[]" }, { "internalType": "string[]", "name": "locations", "type": "string[]" }, { "internalType": "uint256[]", "name": "dates", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "times", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "totalTickets", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "ticketPrices", "type": "uint256[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getEventCount", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_eventId", "type": "uint256" } ], "name": "getEventDetails", "outputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "string", "name": "location", "type": "string" }, { "internalType": "uint256", "name": "date", "type": "uint256" }, { "internalType": "uint256", "name": "time", "type": "uint256" }, { "internalType": "uint256", "name": "totalTickets", "type": "uint256" }, { "internalType": "uint256", "name": "ticketPrice", "type": "uint256" } ], "stateMutability": "view", "type": "function" } ]' )  # Your ABI here

        simple_storage = w3.eth.contract(address=contract_address, abi=contract_abi)
        nonce = w3.eth.get_transaction_count(my_address)

        print("transaction success")

        try:
            # Create a transaction to interact with the contract
            greeting_transaction = simple_storage.functions.createEvent(
                name, location, date, time, total_tickets, ticket_price
            ).buildTransaction(
                {
                    "chainId": w3.eth.chain_id,
                    "gas": 700000,
                    "gasPrice": w3.eth.gas_price,
                    "from": my_address,
                    "nonce": nonce + 1,
                }
            )

            # Sign the transaction
            signed_txn = w3.eth.account.sign_transaction(greeting_transaction, private_key=private_key)

            # Send the signed transaction to the network
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

            # Wait for the transaction to be mined
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            print(tx_receipt.get('transactionHash'))
        except Exception as e:
            print(f"Error: {e}")
    return render(request, "host.html")

def event_detail(request):
    return render(request,"event_detail.html")
    