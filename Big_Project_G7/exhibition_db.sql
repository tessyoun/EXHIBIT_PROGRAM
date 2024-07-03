-- Customer Table
CREATE TABLE Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerType ENUM('Individual', 'Corporate') NOT NULL,
    CustomerName VARCHAR(255) NOT NULL,
    CustomerContact VARCHAR(255) NOT NULL
);

-- Chat History Table
CREATE TABLE ChatHistory (
    ChatID INT AUTO_INCREMENT PRIMARY KEY,
    ChatTimestamp DATETIME NOT NULL,
    Inquiry TEXT,
    Response TEXT,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Reservation History Table
CREATE TABLE ReservationHistory (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    ProgramTimeID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
    -- FOREIGN KEY (ProgramTimeID) REFERENCES ProgramTime(ProgramTimeID) -- Assuming ProgramTime table exists
);

-- Exhibition Table
CREATE TABLE Exhibition (
    ExhibitionID INT AUTO_INCREMENT PRIMARY KEY,
    ExhibitionName VARCHAR(255) NOT NULL,
    ExhibitionDescription TEXT,
    ExhibitionRegistrationDate DATE
);

-- Ticket Info Table
CREATE TABLE TicketInfo (
    TicketID INT AUTO_INCREMENT PRIMARY KEY,
    ExhibitionID INT,
    Audience ENUM('Adult', 'Child') NOT NULL,
    Price DECIMAL(10, 2),
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibition(ExhibitionID)
);

-- Reservation Info Table
CREATE TABLE ReservationInfo (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    ExhibitionID INT,
    TicketID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibition(ExhibitionID),
    FOREIGN KEY (TicketID) REFERENCES TicketInfo(TicketID)
);

-- Exhibition Organizer Table
CREATE TABLE ExhibitionOrganizer (
    OrganizerID INT AUTO_INCREMENT PRIMARY KEY,
    OrganizerName VARCHAR(255) NOT NULL,
    OrganizerCompany VARCHAR(255) NOT NULL,
    OrganizerContact VARCHAR(255) NOT NULL
);

-- Program Table
CREATE TABLE Program (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY,
    ProgramName VARCHAR(255) NOT NULL,
    ProgramDescription TEXT,
    BoothID INT,
    ParentProgramID INT,
    FOREIGN KEY (BoothID) REFERENCES Booth(BoothID)
    -- FOREIGN KEY (ParentProgramID) REFERENCES Program(ProgramID) -- Assuming hierarchical relationship
);

-- Booth Table
CREATE TABLE Booth (
    BoothID INT AUTO_INCREMENT PRIMARY KEY,
    BoothName VARCHAR(255) NOT NULL,
    CompanyID INT,
    ExhibitionID INT,
    ExhibitionCategory VARCHAR(255),
    BoothDescription1 TEXT,
    BoothDescription2 TEXT,
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibition(ExhibitionID)
);

-- Booth Addition Table
CREATE TABLE BoothAddition (
    BoothAdditionID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    BoothID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (BoothID) REFERENCES Booth(BoothID)
);

-- Notice Table
CREATE TABLE Notice (
    NoticeID INT AUTO_INCREMENT PRIMARY KEY,
    AuthorName VARCHAR(255) NOT NULL,
    Title VARCHAR(255) NOT NULL,
    Content TEXT,
    Reason TEXT,
    RegistrationDate DATETIME,
    ExhibitionID INT,
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibition(ExhibitionID)
);

-- Exhibition Hall Table
CREATE TABLE ExhibitionHall (
    ExhibitionHallID INT AUTO_INCREMENT PRIMARY KEY,
    HallDescription TEXT
);
