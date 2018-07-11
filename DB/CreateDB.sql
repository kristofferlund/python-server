IF OBJECT_ID('Users', 'U') IS NOT NULL
    DROP TABLE Users;

-- Create User table
CREATE TABLE Users
(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName   NVARCHAR(25) NOT NULL,
    LastName   NVARCHAR(25) NOT NULL,
    DisplayName NVARCHAR(16) NOT NULL,
)

IF OBJECT_ID('Rooms', 'U') IS NOT NULL
    DROP TABLE Rooms;
    
-- Create Rooms table
CREATE TABLE Rooms
(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    RoomName   NVARCHAR(50) NOT NULL,
) 
