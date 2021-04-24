title: Vehicle Search In India For Open Source Intelligence (OSINT)
date: 13 Apr 21
research: research
tagosint: osint
tagtraining: training
author: ka4n6
description: Unfortunately vehicle numbers are diverse across the globe leading to requirement of local resources to identify the country where vehicle is registered and also identify the owner of the vehicle.



[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)]()	 [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]() 	[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)]()

In collecting OSINT to identify vehicle or persons, searching vehicle number plates is one of the important tasks. But unfortunately vehicle numbers are diverse across the globe leading to requirement of local resources to identify the country where vehicle is registered and also identify the owner of the vehicle. Hence the vehicle search tools used in variuos international and US based OSINT courses may not help in searching plates in India. In Indian scenario vehicle registration is state specific but vehicle searc can be done for the country and no need to search in every state.

**Vehicle search can be used in OSINT work for following purposes:**

>    - Identify owner name and approximate location for further intelligence collection
>    - Identify criminal/victim associated with a crime/incident
>    - Identify approximate location where a photo was taken based on vehicle in the photo
>    - To confirm movement of a target in a particular area
>    - and so on

**A vehicle number will consist of 4 parts. For example: KL 18 X 9570**;

   - First two (KL) alphabetic letters indicate the state or union territory
   - Next two digit numbers (18) indicate district or Road Transport Office (RTO) of registration.
   - Third part (X) may consist of one or two or three alphabetic letters. This shows the ongoing series of a district/RTO. Some vehicles especially older ones may not have third part (i.e., There may not be any letter at all )
   - Fourth part (9570) is usually a four digit number ranging from 1 to 9999. However additional letters may be prefixed when 4 digit numbers run out.

Please read this [Wiki page](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_India) to understand different colours used for plates and variation from standard formats for special vehicles like Army vehicles, Consulate vehicles, UN vehicles etc.

Please find State/Union Territory codes and RTO codes [here](https://en.wikipedia.org/wiki/List_of_Regional_Transport_Office_districts_in_India)

### [Go Digit](https://www.godigit.com/traffic-rules/how-to-find-vehicle-owner-details-by-registration-number)
This is an excellent tool to search and find vehicle owner. In fact it provides owner's private data and also some data related to vehicle including Chassis Number and Engine Number. But major setback is that it requires a valid mobile phone number requiring validation through OTP to fetch vehicle details.

>![Screenshot of vehicle search on Go Digit](\static\research\godigit1.png)

### [Vahan E-services](https://vahan.nic.in/nrservices/faces/user/citizen/citizenlogin.xhtml)
This is a government site managed by Ministry of Road Transport & Highways, Government of India. Though this portal requires registration with valid email ID and valid phone number, provides authentic information on a vehicle.

>![Screenshot of information obtained from Vahan E-services](\static\research\vahan1.png)

### [Vahan Info](https://vahaninfos.com/vehicle-details-by-number-plate)
This provides us basic vehicle details including owner name. Best feature is there no need of creating account and it has simple user interface. You can right away enter vehicle number without space and enter Captcha to directly access the info.

### [Find and Trace](https://www.findandtrace.com/trace-find-vehicle-number-owner-registration)
Find and Trace is general search site with features to search mobile phone numbers, landline numbers, bulk SMS etc. but provides basic searching of vehicle numbers. However the amount of information available is very limited and can not not be compared with other portals discussed above.

### [Drive Spark](https://www.drivespark.com/rto-vehicle-registration-details/)
Enter the vehicle registration number in the search box shown on the website and find out the details of any vehicle registered in India. 

### [Vehicle History](https://vehiclehistory.in/)
Though it requires registration and registration requires active email ID and mobile phone number, it can be used by regular users. Special feature of the website is that it generates a beautiful report with all available information on the vehicle but on payement by subscribing Gold or Platinum certificate. A sample history certificate generated is also given on its home page. 

### [Droom](https://droom.in/history)
Droom is again a good resource but needs validation through email and mobile phone number which is a problem for OSINT analyst. It seems this is a second domain of [Vehicle History](https://vehiclehistory.in/) discussed above.

### [Zoop.One](https://zoop.one/vehicle-rc-verification-api/)
And at the end check out this commercial tool used for vehicle verification. It provides API key for vehicle verification purposes.

### State RTO Websites

All states and union territories have their own websites for road transport. Few examples are:

[Andhra Pradesh](https://aprtacitizen.epragathi.org/#!/vehicleRegistrationSearch)

[Kerala](https://mvd.kerala.gov.in/citizenCorner)

[Madhya Pradesh](http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx)

[Telangana](https://tgtransport.net/TGCFSTONLINE/Reports/VehicleRegistrationSearch.aspx)

[Tripura](https://tsu.trp.nic.in/transport/public/vahan/RegistrationSearch_citz.aspx)

[Andaman and Nicobar](http://db.and.nic.in/mvd/Forms/Regn/RegnDetails.aspx)

[Jharkhand](http://jhtransport.gov.in/vehicle-fitness.html)


However most of the above sites are linked to [Vahan](https://vahan.nic.in/nrservices/faces/user/citizen/citizenlogin.xhtml) site of Government of India for vehicle search purposes.
Utility of these state road transport websites may vary but sites like [Madhya Pradesh](http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx) are very useful furnishing all required information of a vehicle.

### [Gadi Number Se Vahan Malik ka nam Pata kare Android App](https://play.google.com/store/apps/details?id=com.hs.rtovehicledetail.vahan.vehicleregistrationdetails.rtoapp&fbclid=IwAR1us2xUlSYDlVjQy30xLO39RFsHKSYPV7iem6_GQdzdQhhGPKo5uDN2Pu4)

This is a cheap android app by Hangover Studios available on Google Play. Though a buggy app with advertisements it does work without asking for registration or phone number. It partially displays Engine and Chasis numbers but gives us the full name of owner which is great. Information furnished are under following heads;
    - Owner Name
    - Maker Model
    - Registration Date
    - Fuel Type
    - Vehicle Class
    - Registration Authority
    - Engine Number
    - Chasis Number

### [CarInfo - Vehicle Owner Information Android App](https://play.google.com/store/apps/details?id=com.cuvora.carinfo&hl=en_IN&gl=US)
CarInfo is again a great android application to fetch complete vehicle information. I would rate it above all other tools as the amount of information is huge in some vehicles. In addition to the information mentioned above CarInfo gives us extra information under following headings;
        - Ownership (1st owner or 2nd owner and so on)
        - Financers Name (Gives the name of the Bank which provided loan)
        - Vehicle age in years
        - Insurance expiry
        - Color

Above details are very crucial and useful information for an OSINT analyst. This app also has a feature to challan details against the vehicle, but its functionality is questionable as police challans are not yet digitized barring few cities.
This app is also available on iOS [[Click here](https://apps.apple.com/in/app/rto-vehicle-information-india/id1146173741)]


### [RTO Vehicle Information Android App](https://play.google.com/store/apps/details?id=com.vehicle.rto.vahan.status.information.register&hl=en_IN&gl=US)

This android application provides details under three main features i.e., vehicle search, check insurance and driving licence. Though other features are not very effective and useful for OSINT analysts, vehicle search furnishes all essential information including owner name. App contains advertisements which keeps popping up. One problem with this is sometimes complete name is not displayed. Information is not as consistent as CarInfo App.

**Though the amount of information that can be obtained from these portals vary there are some site which can be rated as best among all. Though [Vahan E-services](https://vahan.nic.in/nrservices/faces/user/citizen/citizenlogin.xhtml) is a government database gives authentic information, site [Go Digit](https://www.godigit.com/traffic-rules/how-to-find-vehicle-owner-details-by-registration-number) provides maximum information including age and color of the vehicle. Further android application ['CarInfo - Vehicle Owner Information'](https://play.google.com/store/apps/details?id=com.cuvora.carinfo&hl=en_IN&gl=US) can rated as best as far as vehicle search is concerned.** 