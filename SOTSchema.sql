DROP TABLE IF EXISTS InvestInstruction;
DROP TABLE IF EXISTS ETF;
DROP TABLE IF EXISTS Administrator;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Frequency;

CREATE TABLE Customer
(
	Login			VARCHAR(20)		PRIMARY KEY,
	Password		VARCHAR(40)		NOT NULL,
	FirstName		VARCHAR(20)		NOT NULL,
	LastName		VARCHAR(20)		NOT NULL,
	Email			VARCHAR(50)     NOT NULL,
	CashBalance		DECIMAL(12,2)
);

INSERT INTO Customer VALUES ('amishigan', '0000', 'Adam', 'Mishigan', 'adam.m@gmail.com', 25750.80);
INSERT INTO Customer VALUES ('akellup', '1111', 'Ali', 'Kellup', 'akellup@yahoomail.com', 7100.00);
INSERT INTO Customer VALUES ('cbowtel', '2222', 'Carie', 'Bowtel', 'cbowtel59@gmail.com', 17800.50);
INSERT INTO Customer VALUES ('jswift', '3333', 'James', 'Swift', 'james_swift@hotmail.com', 12300.30);
INSERT INTO Customer VALUES ('kkatana', '4444', 'Kim', 'Katana', 'kkatana@gmail.com', 6000.00);
INSERT INTO Customer VALUES ('mchan2', '5555', 'Maggie', 'Chan', 'maggie_chan@msn.com', 3000.00);
INSERT INTO Customer VALUES ('opalster', '6666', 'Oliver', 'Palster', 'oliver.palster@hotmail.com', 8370.69);
INSERT INTO Customer VALUES ('jkeller', '7777', 'Jack', 'Keller', 'jkeller72@msn.com', 12471.80);

CREATE TABLE Administrator
(
	Login			VARCHAR(20)		PRIMARY KEY,
	Password		VARCHAR(40)		NOT NULL,
	FirstName		VARCHAR(20)		NOT NULL,
	LastName		VARCHAR(20)		NOT NULL,
	Email			VARCHAR(50)     NOT NULL,
	Remuneration	DECIMAL(12,2)	NOT NULL CHECK (Remuneration > 0)
);

INSERT INTO Administrator VALUES ('bshell5', 'adm000', 'Benjamin', 'Shell', 'benjamin.shell@gmail.com', 92300.80);
INSERT INTO Administrator VALUES ('ciori', 'adm111', 'Candice', 'Iori', 'kiori59@hotmail.com', 120550.90);
INSERT INTO Administrator VALUES ('daegis', 'adm222', 'Derien', 'Aegis', 'derien.aegis@yahoomail.com', 95700.15);
INSERT INTO Administrator VALUES ('hgood', 'adm333', 'Hemdall', 'Good', 'hemdall_good@gmail.com', 97990.45);
INSERT INTO Administrator VALUES ('nsmith', 'adm444', 'Nick', 'Smith', 'nsmith774@yahoomail.com', 109915.10);
INSERT INTO Administrator VALUES ('ppan', 'adm555', 'Peter', 'Pan', 'ppan90@gmail.com', 108915.10);
INSERT INTO Administrator VALUES ('rpacca', 'adm666', 'Ricardo', 'Pacca', 'ric.pacca@hotmail.com', 88350.70);
INSERT INTO Administrator VALUES ('sholly', 'adm777', 'Shaz', 'Holly', 'sholly83@gmail.com', 94660.75);

CREATE TABLE ETF
(
	Code				VARCHAR(5)		PRIMARY KEY,
	Name				VARCHAR(50)		NOT NULL,
	Description			VARCHAR(200)	NOT NULL
);

INSERT INTO ETF VALUES ('A200', 'BetaShares A200', 'Tracks the return of the 200 largest ASX companies (not the index specifically).');
INSERT INTO ETF VALUES ('AAA', 'Australian High Interest Cash', 'Opportunity to earn attractive monthly income from Australian cash, in a single ASX trade.');
INSERT INTO ETF VALUES ('ACDC', 'ETFS Battery Tech & Lithium', 'Provides investors with access to companies involved in battery technology and lithium mining.');
INSERT INTO ETF VALUES ('AGVT', 'Australian Government Bond', 'Portfolio diversification and regular monthly income from a portfolio of high-quality Australian government bonds.');
INSERT INTO ETF VALUES ('AQLT', 'Australian Quality', 'Invest in a portfolio of Australia’s highest quality companies, in a single ASX trade.');
INSERT INTO ETF VALUES ('BILL', 'iShares Core Cash', 'Capital preservation and regular income with a diversified portfolio of high quality short-term money market instruments.');
INSERT INTO ETF VALUES ('BNKS', 'Global Banks', 'A simple and cost-effective way to gain exposure to a diversified portfolio of the world’s largest banks in a single ASX trade.');
INSERT INTO ETF VALUES ('CLDD', 'BetaShares Cloud Computing', 'Provides exposure to leading companies in the global cloud computing industry.');
INSERT INTO ETF VALUES ('CURE', 'ETFS S&P Biotech', 'Exposure to the US biotechnology sub-industry within the health care sector.');
INSERT INTO ETF VALUES ('EEU', 'BetaShares Euro ETF', 'Tracks the change in price of the Euro relative to the Australian dollar.');
INSERT INTO ETF VALUES ('ETHI', 'Global Sustainability Leaders', 'Get diversified exposure to a portfolio of large global companies that meet strict sustainability and ethical standards.');
INSERT INTO ETF VALUES ('F100', 'BetaShares FTSE 100 ETF', 'Provides exposure to the largest 100 companies by market capitalisation traded on the London Stock Exchange.');
INSERT INTO ETF VALUES ('GOLD', 'ETFS Physical Gold', 'Provides a return equivalent to the movements in the gold spot price.');
INSERT INTO ETF VALUES ('IAA', 'iShares Asia 50', 'Provides exposure to 50 of the largest Asian companies located in China, Hong Kong, Macau, Singapore, South Korea and Taiwan.');
INSERT INTO ETF VALUES ('IEU', 'iShares Europe', 'Broad exposure to large, mid and small capitalisation companies in Europe.');
INSERT INTO ETF VALUES ('IGB', 'iShares Treasury', 'Composed of fixed income bonds issued by the Australian Treasury.');
INSERT INTO ETF VALUES ('IIND', 'BetaShares India Quality', 'Tracks the 30 highest quality Indian companies based on a combined ranking of high profitability, low leverage and high earnings stability.');
INSERT INTO ETF VALUES ('IJP', 'iShares MSCI Japan', 'The fund seeks to track the investment results of an index composed of Japanese equities.');
INSERT INTO ETF VALUES ('IXJ', 'iShares Global Healthcare', 'Composed of global equities in the Healthcare sector.');
INSERT INTO ETF VALUES ('IYLD', 'Ishares Yield Plus', 'Track the performance of the Australian corporate bond market (excluding issuers ANZ, CBA, NAB and WBC).');
INSERT INTO ETF VALUES ('OOO', 'Crude Oil Index', 'Exposure to crude oil futures, as simply as buying any share on the ASX.');
INSERT INTO ETF VALUES ('QUS', 'S&P 500 Equal Weight', 'Portfolio of 500 leading U.S. companies that aims to outperform the market cap-weighted S&P 500 Index.');
INSERT INTO ETF VALUES ('SFY', 'SPDR S&P/ASX 50', 'Tracks the return of the S&P/ASX 50 Index.');
INSERT INTO ETF VALUES ('USD', 'BetaShares U.S. Dollar', 'Tracks the change in price of the US Dollar relative to the Australian dollar.');
INSERT INTO ETF VALUES ('YANK', 'Strong U.S. Dollar Fund', 'A simple and convenient way to gain geared exposure to the value of the U.S. dollar relative to the Australian dollar.');

CREATE TABLE Frequency
(
	FrequencyCode	VARCHAR(5)		PRIMARY KEY,
	FrequencyDesc	VARCHAR(30)		NOT NULL UNIQUE
);

INSERT INTO Frequency (FrequencyCode, FrequencyDesc) VALUES ('FTH', 'Fortnightly');	-- 1
INSERT INTO Frequency (FrequencyCode, FrequencyDesc) VALUES ('MTH', 'Monthly');		-- 2

CREATE TABLE InvestInstruction
(
	InstructionId	SERIAL			PRIMARY KEY,
	Amount			DECIMAL(12,2)	NOT NULL,
	Frequency		VARCHAR(5)		NOT NULL,
	ExpiryDate		DATE			NOT NULL,
	Customer		VARCHAR(20)		NOT NULL,
	Administrator	VARCHAR(20),
	Code			VARCHAR(5)		NOT NULL,
	Notes			VARCHAR(200),
	FOREIGN KEY (Frequency) REFERENCES Frequency,
	FOREIGN KEY (Customer) REFERENCES Customer,
	FOREIGN KEY (Administrator) REFERENCES Administrator,
	FOREIGN KEY (Code) REFERENCES ETF
);

INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (2200, 'MTH', '28/01/2023', 'amishigan', 'hgood', 'IXJ', NULL);											--1
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (1880, 'FTH', '04/10/2023', 'cbowtel', 'ciori', 'A200', NULL);			                                --2
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (5250, 'MTH', '15/05/2022', 'kkatana', 'ppan', 'CURE', 'Client didn''t want renew regular investment.');	--3
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (2400, 'FTH', '24/02/2023', 'jkeller', NULL, 'SFY', NULL);												--4
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (1500, 'FTH', '27/01/2023', 'jswift', 'ciori', 'BNKS', 'Follow up with customer in 2 months time.');		--5
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (2890, 'FTH', '17/04/2023', 'opalster', 'ppan', 'GOLD', 'Client wants to reduce amount next month.');	--6
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (3170, 'MTH', '24/02/2023', 'cbowtel', 'ciori', 'IJP', 'Client wants to increase investment amount.');	--7
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (4600, 'FTH', '06/07/2022', 'akellup', NULL, 'CLDD', NULL);												--8
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (1400, 'MTH', '26/06/2022', 'mchan2', 'ciori', 'IYLD', 'Instruction not renewed.');	                	--9
INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) VALUES (2400, 'FTH', '19/12/2023', 'mchan2', NULL, 'SFY', 'Previous instruction was cancelled.');	        	--10

COMMIT;