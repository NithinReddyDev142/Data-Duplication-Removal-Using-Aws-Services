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






