# project5550_a00447454-   REST API Project

### Sunaritha Rajendra Karanth - A00447454

**API for hotel reservation system using Python Django rest framework**

## Get: Get List of hotels available in database
http://localhost:8000/getListOfHotels/

Response: 
```
[
    {
        "name": "Taj",
        "price": 1998,
        "available": 1
    }
]
```
## Post: Reservation Confirmation.

parameters: 
- hotelname(String)- Hotel name.
- checkin_date(String)- Check in Date.
- checkout_date(String)- Check out Date.
- guests_list (list):
    - guest_name(String)- Name of Guest
    - gender(String)- Gender of Guest
            
http://localhost:8000/reservationConfirmation/

Example:
```
{
    "hotelname":"Taj",
    "checkin_date":"8-9-1908",
    "checkout_date": "10-10-1908",
    "guests_list": [{"guest_name": "Tom", "gender":"Female"}]
}
```

Response: 
```
{
    "confirmation_number": 3
}
```
