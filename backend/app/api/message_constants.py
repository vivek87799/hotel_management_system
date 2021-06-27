class CustomErrorMessage:
    BOOKING_DOES_NOT_EXIST = {"message": "No Booking is done for the hotel"}
    MAXIMUM_BOOKING_FOR_THE_HOTEL = {"message": "Booking for the hotel is full"}
    BOOKING_NOT_AUTHORIZED_FOR_THE_HOTEL = {"message": "Booking is not authorized for this hotel by LIMEHOME"}
    NO_HOTEL_AVAILABLE_IN_DATABASE = {"message": "No hotel is persisted on the database"}

class CustomSuccessMessage:
    BOOKING_SCCESSFULL = {"message": "Your booking has been accepted"}
    NO_HOTELS_AVAILABLE_FOR_THE_POSITION = {"message": "No hotel available for the given position"}