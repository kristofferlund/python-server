IF OBJECT_ID('Users', 'U') IS NOT NULL
    DROP TABLE Users;

-- Create User table
CREATE TABLE Users
(
    DisplayName NVARCHAR(16) NOT NULL,
    FirstName   NVARCHAR(25) NOT NULL,
    LastName   NVARCHAR(25) NOT NULL,
    ID INT IDENTITY(1,1) PRIMARY KEY,
)

IF OBJECT_ID('Rooms', 'U') IS NOT NULL
    DROP TABLE Rooms;
    
-- Create Rooms table
CREATE TABLE Rooms
(
    RoomName   NVARCHAR(50) NOT NULL,
    ID INT IDENTITY(1,1) PRIMARY KEY,
) 