-- made from chatgpt
-- only used for making db.sqlite3
-- Enable foreign key support
PRAGMA foreign_keys = ON;

-- Customer Table
CREATE TABLE Customer (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerType TEXT CHECK(CustomerType IN ('Individual', 'Corporate')) NOT NULL,
    CustomerName VARCHAR(255) NOT NULL,
    CustomerContact VARCHAR(255) NOT NULL
);

-- Chat History Table
CREATE TABLE ChatHistory (
    ChatID INTEGER PRIMARY KEY AUTOINCREMENT,
    ChatTimestamp DATETIME NOT NULL,
    Inquiry TEXT,
    Response TEXT,
    CustomerID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Reservation History Table
CREATE TABLE ReservationHistory (
    ReservationID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    ProgramTimeID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
    -- FOREIGN KEY (ProgramTimeID) REFERENCES ProgramTime(ProgramTimeID) -- Assuming ProgramTime table exists
);

-- Exhibition Table
CREATE TABLE Exhibition (
    ExhibitionID INTEGER PRIMARY KEY AUTOINCREMENT,
    ExhibitionName VARCHAR(255) NOT NULL,
    ExhibitionDescription TEXT,
    ExhibitionRegistrationDate DATE
);

-- Ticket Info Table
CREATE TABLE TicketInfo (
    TicketID INTEGER PRIMARY KEY AUTOINCREMENT,
    ExhibitionID INTEGER,
    Audience TEXT CHECK(Audience IN ('Adult', 'Child')) NOT NULL,
    Price DECIMAL(10, 2),
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibition(ExhibitionID)
);

-- Reservation Info Table
CREATE TABLE ReservationInfo (
    ReservationID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    ExhibitionID INTEGER,
    TicketID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibition(ExhibitionID),
    FOREIGN KEY (TicketID) REFERENCES TicketInfo(TicketID)
);

-- Exhibition Organizer Table
CREATE TABLE ExhibitionOrganizer (
    OrganizerID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrganizerName VARCHAR(255) NOT NULL,
    OrganizerCompany VARCHAR(255) NOT NULL,
    OrganizerContact VARCHAR(255) NOT NULL
);

-- Booth Table
CREATE TABLE Booth (
    BoothID INTEGER PRIMARY KEY AUTOINCREMENT,
    BoothName VARCHAR(255) NOT NULL,
    CompanyID INTEGER,
    ExhibitionID INTEGER,
    ExhibitionCategory VARCHAR(255),
    BoothDescription1 TEXT,
    BoothDescription2 TEXT,
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibition(ExhibitionID)
);

-- Program Table
CREATE TABLE Program (
    ProgramID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProgramName VARCHAR(255) NOT NULL,
    ProgramDescription TEXT,
    BoothID INTEGER,
    ParentProgramID INTEGER,
    FOREIGN KEY (BoothID) REFERENCES Booth(BoothID)
    -- FOREIGN KEY (ParentProgramID) REFERENCES Program(ProgramID) -- Assuming hierarchical relationship
);

-- Booth Addition Table
CREATE TABLE BoothAddition (
    BoothAdditionID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    BoothID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (BoothID) REFERENCES Booth(BoothID)
);

-- Notice Table
CREATE TABLE Notice (
    NoticeID INTEGER PRIMARY KEY AUTOINCREMENT,
    AuthorName VARCHAR(255) NOT NULL,
    Title VARCHAR(255) NOT NULL,
    Content TEXT,
    Reason TEXT,
    RegistrationDate DATETIME,
    ExhibitionID INTEGER,
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibition(ExhibitionID)
);

-- Exhibition Hall Table
CREATE TABLE ExhibitionHall (
    ExhibitionHallID INTEGER PRIMARY KEY AUTOINCREMENT,
    HallDescription TEXT
);
