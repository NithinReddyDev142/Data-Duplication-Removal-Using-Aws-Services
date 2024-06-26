# Data-Duplication-Removal-Using-Aws-Services
This is my first Project

ABSTRACT:
Cloud computing comes all through core interest advancement of network computing, virtualization just as web advancements. With an expansion in the use of cloud storage, powerful strategies should be utilized to diminish equipment costs, meet the data transmission necessities, and build stockpiling proficiency. This can be accomplished by utilizing Data Deduplication. Using this, less information will be on the server thus require less equipment and users would have the option to put more data in the additional space available. At present utilization of cloud storage is expanding and to conquer expanding information issues, Data deduplication methods are utilized. Information Deduplication methods can’t be applied straightforwardly with security instruments. 
In this paper, we are eliminating copy information to save storage space and speed up the organization. Here we applied MD5 hashing to generate a hash value (when uploaded to cloud storage) and then compare those with values (when the same file uploaded with a different name) to find out the duplicate data in the cloud environment. When deduplication is accomplished framework plan for secure information change in the organization. Security is accomplished through encryption and decoding of the information. This paper inspects secure deduplication strategy. After removal of duplicate data pointers will give reference to the original file.

PROPOSED SYSTEM:

Presently day information duplication is a quickly developing method used in information reinforcement stored without excess. It is vital special and unique. In this paper, we design an interactive protocol using AWS services in which we use the AWS lambda function for generating the hash value of the file which gets uploaded. We use AWS cloud watch for records of every file, also used the S3 bucket for storing and retrieving the data. We investigated the information to decide the relative adequacy of information deduplication, especially considering the entire record versus the block-level end of excess.  Security in information deduplication can be furnished with the utilization of a concurrent encryption method that encodes the information previously transferred to the public framework. 
To prove the thought, we proposed the model and attempted some tests, in that test we uploaded the same files with different names and different file systems such as pdf, doc, odt. The work shows that the proposed system works correctly and gives a warning that the same file was uploaded before. Cloud computing is productive and adaptable yet keeping up the strength of preparing such countless positions in the distributed computing climate the cloud framework faces the issues of replication furthermore, the information duplication as indicated by situations. In this setting need to tackle the issue of both, to upgrade the cloud execution as far as capacity overhead and accessibility needed to deal with the whole information in such a way by which the hunting capacity and the ordering of information can be accomplished both. 
A.	DATA DEDUPLICATION WORKING 
Data deduplication works by seeing items (ordinarily records or then again squares) and dispenses with objects. Deduplication Process (copies) that as of now exist in the educational assortment. All the cycles which are not uncommon are taken out in this method. In the Data deduplication procedure, we parcel the data into blocks, and hash regard is resolved for all of these squares. By then using these hash regards we can choose if another square of similar data has recently been taken care of. If a commensurate information report is found, reject the copy information with a reference to the article satisfactorily present in the educational record.The process of deduplication is shown in fig.

B.	HASH BASED ALGORITHM 
Hash-based deduplication systems use counts to perceive chunks of data. In case the hash is currently made, the data is perceived as a duplicate and isn’t taken care of. Message Digest Algorithm 5(MD5): This 128-cycle has in like manner expected for cryptographic jobs. In this strategy, the 128-cycle state is divided into four 32-bit words, implied A, B, C, and D. These are acquainted with certain fixed constants. This cycles the ”knot” with hashing estimation to make a hash. If the hash as of now exists, the data is viewed as a duplicate and isn’t taken care of. If the hash doesn’t exist, by then the data is taken care of and the hash record is revived with the hash. The hashing procedure is depicted in Figure. 

C.	DEDUPLICATION IMPROVED TECHNIQUE
 Deduplication is a suitable strategy for the headway of instances of data set aside in disseminated capacity. Deduplication can be requested into lumps level and report level deduplication. Pieces level deduplication procedure approves the limit of uncommon irregularities by taking a gander at each moving toward the piece for duplicate ID. This methodology achieves better deduplication viability since it requests deduplication. 

D.	PROPOSED APPROACH
 The examination issue in this paper requires the utilization of quantitative techniques for estimating, positioning, arranging, distinguishing examples, and making speculations. We want to find a way to give each file and unique hash ID stored in the Amazon S3 bucket and use that id to compare with the newly uploaded/collected files. Another Lambda Function to successfully implement the Data Deduplication. The proposed approach is depicted in Figure.

EXISTING SYSTEM:
To study the data breaches in cloud storage, a study was carried by. Various instances of breaches were found where the data of the client was exposed by the service providers. The instances exposed that if the service provider or the client has access to data of other users the breaching of data was more. For handling the data breach problem, the authors suggested end-to-end encryption. The issues in deduplication while encryption were found by authors in. To resolve they proposed a novel encryption methodology. In the methodology, the encryption units were transformed into chunks and these chunks were used to produce symmetric keys. The symmetric key obtained were used to limit mapping between plain and ciphertext. To reclaim space that was lost during replicating files, a methodology was introduced by. The methodology involved convergent encryption that permitted duplicate files to be consolidated into a single file using diverse user keys and SALAD, a Self Arranging Lossy Association Database. 
The authors in proposed FadeVersion, a system for cloud backup which also can act as a security layer. It was also able to provide cryptographic security to data.


MODULES:


There are 2 modules:
1.	User 
2.	Cloud
User:-
	Register
	Login
	Data Storage
	Data search
	Profiles
	Downloads Files
	Logout
              Cloud:-
	Login
	Manage Users
	View files
	User Authentication




SYSTEM TESTING
Types of Software Testing: Different Testing Types with Details
We, as testers, are aware of the various types of Software Testing like Functional Testing, Non-Functional Testing, Automation Testing, Agile Testing, and their sub-types, etc.
Each type of testing has its own features, advantages, and disadvantages as well. However, in this tutorial, we have covered mostly each and every type of software testing which we usually use in our day-to-day testing life.
Different Types of Software Testing
 

Functional Testing
There are four main types of functional testing.
#1) Unit Testing
Unit testing is a type of software testing which is done on an individual unit or component to test its corrections. Typically, Unit testing is done by the developer at the application development phase. Each unit in unit testing can be viewed as a method, function, procedure, or object. Developers often use test automation tools such as NUnit, Xunit, JUnit for the test execution.
Unit testing is important because we can find more defects at the unit test level.
For example, there is a simple calculator application. The developer can write the unit test to check if the user can enter two numbers and get the correct sum for addition functionality.
a) White Box Testing
White box testing is a test technique in which the internal structure or code of an application is visible and accessible to the tester. In this technique, it is easy to find loopholes in the design of an application or fault in business logic. Statement coverage and decision coverage/branch coverage are examples of white box test techniques.
b) Gorilla Testing
Gorilla testing is a test technique in which the tester and/or developer test the module of the application thoroughly in all aspects. Gorilla testing is done to check how robust your application is.
For example, the tester is testing the pet insurance company’s website, which provides the service of buying an insurance policy, tag for the pet, Lifetime membership. The tester can focus on any one module, let’s say, the insurance policy module, and test it thoroughly with positive and negative test scenarios.
#2) Integration Testing
Integration testing is a type of software testing where two or more modules of an application are logically grouped together and tested as a whole. The focus of this type of testing is to find the defect on interface, communication, and data flow among modules. Top-down or Bottom-up approach is used while integrating modules into the whole system.
This type of testing is done on integrating modules of a system or between systems. For example, a user is buying a flight ticket from any airline website. Users can see flight details and payment information while buying a ticket, but flight details and payment processing are two different systems. Integration testing should be done while integrating of airline website and payment processing system.
a) Gray box testing
As the name suggests, gray box testing is a combination of white-box testing and black-box testing. Testers have partial knowledge of the internal structure or code of an application.
#3) System Testing
System testing is types of testing where tester evaluates the whole system against the specified requirements.
a) End to End Testing
It involves testing a complete application environment in a situation that mimics real-world use, such as interacting with a database, using network communications, or interacting with other hardware, applications, or systems if appropriate.
For example, a tester is testing a pet insurance website. End to End testing involves testing of buying an insurance policy, LPM, tag, adding another pet, updating credit card information on users’ accounts, updating user address information, receiving order confirmation emails and policy documents.
b) Black Box Testing
Blackbox testing is a software testing technique in which testing is performed without knowing the internal structure, design, or code of a system under test. Testers should focus only on the input and output of test objects.
Detailed information about the advantages, disadvantages, and types of Black Box testing can be found here.


