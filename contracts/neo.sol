// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EventContract {
    address public owner;
    
    event TicketPurchased(address indexed buyer, uint256 numTickets);

    struct Event {
        string name;
        string location;
        uint256 date;
        uint256 time;
        uint256 totalTickets;
        uint256 ticketPrice;
    }

    Event[] public events;

    function createEvent(
        string memory _name,
        string memory _location,
        uint256 _date,
        uint256 _time,
        uint256 _totalTickets,
        uint256 _ticketPrice
    ) external {
        events.push(Event({
            name: _name,
            location: _location,
            date: _date,
            time: _time,
            totalTickets: _totalTickets,
            ticketPrice: _ticketPrice
        }));
    }

    function getEventCount() external view returns (uint256) {
        return events.length;
    }

    function getEventDetails(uint256 _eventId) external view returns (
        string memory name,
        string memory location,
        uint256 date,
        uint256 time,
        uint256 totalTickets,
        uint256 ticketPrice
    ) {
        require(_eventId < events.length, "Event does not exist");
        Event memory eventDetails = events[_eventId];
        return (
            eventDetails.name,
            eventDetails.location,
            eventDetails.date,
            eventDetails.time,
            eventDetails.totalTickets,
            eventDetails.ticketPrice
        );
    }
    
    function getAllEventDetails() external view returns (
        string[] memory names,
        string[] memory locations,
        uint256[] memory dates,
        uint256[] memory times,
        uint256[] memory totalTickets,
        uint256[] memory ticketPrices
    ) {
        uint256 eventCount = events.length;

        names = new string[](eventCount);
        locations = new string[](eventCount);
        dates = new uint256[](eventCount);
        times = new uint256[](eventCount);
        totalTickets = new uint256[](eventCount);
        ticketPrices = new uint256[](eventCount);

        for (uint256 i = 0; i < eventCount; i++) {
            Event memory eventDetails = events[i];
            names[i] = eventDetails.name;
            locations[i] = eventDetails.location;
            dates[i] = eventDetails.date;
            times[i] = eventDetails.time;
            totalTickets[i] = eventDetails.totalTickets;
            ticketPrices[i] = eventDetails.ticketPrice;
        }
    }

    function buyTickets(uint256 _eventId, uint256 _numTickets, address _destination) external payable {
        require(_eventId < events.length, "Event does not exist");
        Event storage eventDetails = events[_eventId];
        require(_numTickets > 0, "Number of tickets must be greater than 0");
        require(_numTickets <= eventDetails.totalTickets, "Not enough tickets available");
        require(msg.value >= eventDetails.ticketPrice * _numTickets, "Insufficient payment");
        
        eventDetails.totalTickets -= _numTickets;

        // Emit an event to log the ticket purchase.
        emit TicketPurchased(msg.sender, _numTickets);

        // Calculate the payment amount
        uint256 paymentAmount = eventDetails.ticketPrice * _numTickets;

        // Transfer the payment to the specified destination address
        if (_destination == address(0)) {
            payable(owner).transfer(paymentAmount); // Send to contract owner
        } else {
            payable(_destination).transfer(paymentAmount); // Send to user-specified address
        }
    }

    function getRemainingTickets(uint256 _eventId) external view returns (uint256) {
        require(_eventId < events.length, "Event does not exist");
        return events[_eventId].totalTickets;
    }
}
