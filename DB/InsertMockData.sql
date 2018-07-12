INSERT INTO Users
    ([DisplayName], [FirstName], [LastName])
VALUES
    ('Difee', 'Kristoffer', 'Lund'),
    ('FunTrollz', 'Troll', 'Trollesen')

SELECT * FROM Users;

INSERT INTO Rooms
    ([RoomName])
VALUES
    ('Random'),
    ('Private chat'),
    ('Music talk'),
    ('SharingCaring')

SELECT * FROM Rooms

INSERT INTO UserRoom
    ([UserID], [RoomID])
VALUES
    (1, 1),
    (2, 1),
    (1, 2)

SELECT * FROM UserRoom