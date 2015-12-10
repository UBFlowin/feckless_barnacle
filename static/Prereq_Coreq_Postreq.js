function addCourseAttributes() {
		
		$("#UBE101").attr({title: "University Experience"});
		
		// MATH COURSES
		$("#CALC1").attr({});
		$("#CALC2").attr({pre:"CALC1"});
		
		$("#MTH141").attr({title: "College Calculus I"});
		$("#MTH142").attr({title: "College Calculus II", pre: "MTH141"});	
		$("#MTH241").attr({title: "College Calculus III", pre: "MTH142"});
		$("#MTH306").attr({title: "Intro to Differential Equations", pre: "MTH142"});
		$("#MTH309").attr({title: "Introductory Linear Algebra", pre: "MTH142"});
		$("#MTH417").attr({title: "Survey Of Multivariable Calc", pre: "MTH241"});
		$("#MTH418").attr({title: "Survey Of Partial Differential EQ", pre:"MTH306"});
		
		// SCIENCE COURSES
		
		$("#BIO201").attr({title: "Cell Biology"});
		$("#BIO205").attr({title: "Fundamentals of Biological Chem",pre:'CHE201 CHE203 CHE251'});
		$("#BIO309").attr({title: "Ecology", pre:"BIO200"});
		$("#BIO400").attr({title: "Bioinformatics / Genome Analysis",pre:'BIO319'});
		
		$("#CHE101").attr({title: "Chemistry I"});
		$("#CHE102").attr({title: "Chemistry II", pre: "CHE101"});
		$("#CHE107").attr({title: "Chemistry I"});
		$("#CHE108").attr({title: "Chemistry II", pre: "CHE107"});
		$("#CHE203").attr({title: "Organic Chemistry", pre: "CHE107 CHE108"});
		$("#CHE334").attr({title: "Physical Chemistry for CE", pre: "CE304 MTH142"});
		$("#MIC301").attr({title: "Microbiology"});
		
		$("#GLY309").attr({title: "Ecology", pre:"BIO200"});
		$("#GLY414").attr({title: "Hydrogeology", co: "CIE354"});
		
		$("#PHY107").attr({title: "General Physics I", co: "MTH141"});
		$("#PHY108").attr({title: "General Physics II", co: "MTH142 PHY158", pre: "PHY107"});
		$("#PHY158").attr({title: "General Physics II Lab", co: "PHY108", pre:"PHY107"});
		$("#PHY207").attr({title: "General Physics III", co: "MTH241", pre:"PHY108"});
		$("#PHY208").attr({title: "General Physics IV", pre:"PHY107 PHY108", co:"MTH306"});
		$("#PHY257").attr({title: "General Physics III Lab", co: "MTH241", pre:"PHY108 PHY158"});
		$("#PHY301").attr({title: "Intermediate Mechanics I", pre:"PHY107 MTH306"});
		$("#PHY307").attr({title: "Modern Physics Lab", pre:"PHY207 PHY208 PHY257"});
		$("#PHY401").attr({title: "Modern Physics I", pre:"MTH306 PHY207 PHY208"});
		$("#PHY402").attr({title: "Modern Physics II", pre:"PHY401"});
		$("#PHY403").attr({title: "Electricity And Magnetism I", pre:"MTH241 MTH306 PHY108"});
		$("#PHY404").attr({title: "Electricity And Magnetism II", pre:"PHY403"});
		$("#PHY405").attr({title: "Thermal And Statistical Physics I", pre:"MTH306 PHY208 PHY301"});
		$("#PHY408").attr({title: "Advanced Laboratory", pre:"PHY207 PHY208 PHY257 PHY307 PHY401"});
		//ADDED 2.20.14
		//$("#Soil Science Elective").attr({title: "GLY414(recommended)"});
		
		// EAS COURSES
		
		$("#EAS140").attr({title: "Engineering Principles"});
		$("#EAS202").attr({title: "Engineering Impact on Society", pre: "EAS140"});
		$("#EAS207").attr({title: "Statics", pre: "PHY107 MTH142", co: "MTH241"});
		$("#EAS208").attr({title: "Dynamics", pre: "EAS207 MTH241 I-EAS207", co: "MTH306"});
		$("#EAS209").attr({title: "Mechanics of Solids", pre: "EAS207 I-EAS207"});
		$("#EAS230").attr({title: "Engineering Computation", pre: "MTH141"});
		$("#EAS305").attr({title: "Applied Probability", pre: "MTH241"});
		
		
		// BE COURSES
		
		$("#BE101").attr({title: "Biomedical Eng Seminar"});
		$("#BE201").attr({title: "Principles Of Biomedical Eng", pre: " BE101"});	
		$("#BE202").attr({title: "Applied Medical And Engineering Biology", pre: "BE201"});	
		$("#BE301").attr({title: "Biomedical Engineering Lab 1", pre: "BE201"});	
		$("#BE302").attr({title: "Biomedical Engineering Lab 2", pre: "BE301"});	
		$("#BE304").attr({title: "Principles Of Medical Imaging", pre: "BE202"});	
		$("#BE305").attr({title: "Biomaterials And Mechanics", pre: "PHY108 PHY158 BE201"});	
		$("#BE307").attr({title: "Biomedical Circuits And Signals", pre: "EAS230 BE201 PHY108 PHY158"});	
		$("#BE308").attr({title: "Biofluid Mechanics", pre: "BE301 BE305"});	
		$("#BE309").attr({title: "Biomedical Chemical Principles 1", pre: "CHE108 BE201 BE202"});	
		$("#BE310").attr({title: "Biomedical Chemical Principles 2", pre: "BE309"});	
		$("#BE403").attr({title: "Biomedical Instrumentation", pre: "BE302 BE304 BE307"});	
		$("#BE405").attr({title: "Transport Processes In Biomedical Eng", pre: "BE310 BE308"});	
		$("#BE406").attr({title: "Biomedical Systems Engineering", pre: "BE202 MTH306 EAS305 BE308"});	
		$("#BE494").attr({title: "Senior Capstone Design Project", pre: "BE302"});	
		$("#BE493").attr({title: "Research and Design"});	
		$("#BE498").attr({title: "Undergraduate Research", pre: "BE302"});	
		
		// CIE COURSES
		
		$("#CIE101").attr({title: "Intro to Civil Engineering"});
		$("#CIE303").attr({title: "Geodesy, GPS, & GIS", pre: "MAE177"});
		$("#CIE308").attr({title: "Engineering Statistics", pre: "MTH241 "});
		$("#CIE323").attr({title: "Structural Engineering I", pre: "EAS209"});
		$("#CIE324").attr({title: "Structural Engineering II", pre: "CIE323"});
		$("#CIE325").attr({title: "Structural Engineering II", pre: "CIE323"});
		$("#CIE327").attr({title: "Civil Engineering Materials", pre: "EAS209"});
		$("#CIE334").attr({title: "Soil Mechanics", pre: "EAS209"});
		$("#CIE340").attr({title: "Environmental Engineering", pre:"CHE107 CHE101 CHE105"});
		$("#CIE341").attr({title: "Environmental Engineering Science", pre: "CHE108 CHE102 CHE106 MTH142 CIE340"});
		$("#CIE343").attr({title: "Hydraulic Engineering", pre: "CIE354"});
		$("#CIE354").attr({title: "Fluid Mechanics", pre: "EAS207 I-EAS207", co: "MTH306"});
		$("#CIE360").attr({title: "Environmental Eng Lab", co: "CIE354"});
		$("#CIE361").attr({title: "Civil Eng Lab I", co: "CIE327 I-CIE327 CIE323 CIE354"});
		$("#CIE362").attr({title: "Civil Eng Lab II", co: "CIE334 CIE340 CIE343"});
		$("#CIE415").attr({title: "Professional Practice Issues", co:"CIE442 TEwDesign CIE428"});
		$("#CIE416").attr({title: "CIE Capstone Design", pre:"CIE415 CIE325"});
		$("#CIE428").attr({title: "Steel Design", pre:"CIE324", co:"CIE415"});
		$("#CIE429").attr({title: "Reinforced Concrete Design", pre:"CIE324"});
		$("#CIE435").attr({title: "Foundation Engineering", pre: "CIE334"});
		$("#CIE439").attr({title: "Transportation Systems Analysis", co:"CIE308"});
		$("#CIE441").attr({title: "Ecological Engineering", pre: "MTH306"});
		$("#CIE442").attr({title: "Treatment Process Engineering", co: "CIE343", pre: "CIE340"});
		$("#CIE444").attr({title: "Hydrologic Engineering", pre: "CIE343", co: "CIE308"});
		$("#CIE445").attr({title: "Groundwater Engineering", pre:"CIE354"});
		$("#CIE447").attr({title: "Sustainability", pre:"CIE340"});
		$("#CIE448").attr({title: "Chemical Principles In Env Engineering", pre:"CIE340"});
		$("#CIE449").attr({title: "Environmental Engineering Design", pre:"CIE444 CIE442 CIE415"});
		$("#CIE469").attr({title: "Hazardous Waste Management", pre:"CIE340"});
		$("#TEwDesign").attr({title: "", pre:"CIE324"});
		
		
		// CE COURSES
		
		$("#CE212").attr({title: "Fundamental Principles of CE", pre:"CHE108 MTH142 PHY107"});
		$("#CE304").attr({title: "Chemical Eng Thermodynamics", pre:"CE212 MTH241"});
		$("#CE317").attr({title: "Transport Processes I", pre:"MTH241 PHY107", co:"MTH306"});
		$("#CE318").attr({title: "Transport Processes II", pre:"CE317 MTH306"});
		$("#CE327").attr({title: "Chemical Eng Lab I", co:"CE317"});
		$("#CE328").attr({title: "Chemical Eng Lab II", co:"CE318"});
		$("#CE329").attr({title: "Chemical Reaction Engineering", pre:"CE212 CE304 MTH306"});
		$("#CE341").attr({title: "Applied CE Math", pre:"EAS230 MTH241",co:"CE212 MTH306"});
		$("#CE404").attr({title: "Chem Eng Product Design", pre:"CE318 CE433"});
		$("#CE407").attr({title: "Separations", pre:"CE212", co:"CE304 CE318"});
		$("#CE408").attr({title: "Chemical Eng Plant Design", pre:"CE318 CE329 CE407 CE434"});
		$("#CE427").attr({title: "Chemical Eng Lab III", pre:"CE318", co:"CE329"});
		$("#CE428").attr({title: "Chemical Eng Lab IV", co:"CE407"});
		$("#CE433").attr({title: "Materials Science & Eng", co:"CE304"});
		$("#CE434").attr({title: "Chemical Systems & Control", pre:"CE212 MTH306"});
		
		// CSE COURSES
		
		$("#CSE115").attr({title: "Intro to Comp Sci Majors I"});
		$("#CSE116").attr({title: "Intro to Comp Sci Majors II", pre:"CSE115"});
		$("#CSE191").attr({title: "Discrete Structures"});
		$("#CSE241").attr({title: "Digital Systems"});
		$("#CSE250").attr({title: "Data Structures", pre:"CSE116 CSE191"});
		$("#CSE305").attr({title: "Intro to Program Languages", pre:"CSE250"});
		$("#CSE321").attr({title: "Real-Time & Embedded OS", pre:"CSE250 CSE241", co:"EE378 EE278"});
		$("#CSE331").attr({title: "Intro to Algorithms", pre:"MTH142 CSE250 CSE191"});
		$("#CSE341").attr({title: "Computer Organization", pre:"CSE241 EE378 EE278"});
		$("#CSE379").attr({title: "Microprocessors & Microcomputers", pre:"CSE241 EE378", co:"CSE380"});
		$("#CSE380").attr({title: "Microprocessors & Microcomputers Lab", pre:"CSE241 EE378", co:"CSE379"});
		$("#CSE396").attr({title: "Intro to Theory of Computation", pre:"CSE191 CSE250 MTH142 MTH141"});
		$("#CSE421").attr({title: "Intro to Operating Systems", pre:"CSE250"});
		$("#CSE442").attr({title: "Software Engineering", pre:"CSE250"});
		$("#CSE453").attr({title: "Hardware/Software Integrated Systems", pre:"CSE442"});
		$("#CSE462").attr({title: "Database Concepts", pre:"CSE250"});
		
		// EE COURSES
		
		$("#EE200").attr({title: "Electrical Eng Concepts Nonmajors", pre: "PHY108", co:"MTH306"});
		$("#EE202").attr({title: "Circuit Analysis I", pre:"MTH142", co:"PHY108"});
		$("#EE203").attr({title: "Circuit Analysis II", pre:"EE202"});
		$("#EE205").attr({title: "Signals & Systems", pre:"EE202"});
		$("#EE278").attr({title: "Digital Principles", pre:"MTH142",co:"EE202 MTH306"});
        $("#EE000").attr({title: "Dummy", pre:"EE202 MTH306"});
		$("#EE303").attr({title: "Signal Analysis & Transform Methods", pre:"EE203 EE202"});
		$("#EE305").attr({title: "Applied Probability", pre: "MTH241"});
		$("#EE310").attr({title: "Electronic Devices & Circuits I", pre:"EE202", co:"EE315 EE352"});
		$("#EE311").attr({title: "Electronic Devices & Circuits II", pre:"EE310"});
		$("#EE312").attr({title: "Basic Electronic Instrumentation", pre:"EE202", co:"EE310"});
		$("#EE324").attr({title: "Applied Electromagnetics", pre:"EE202 MTH241 PHY108 PHY207 PHY257"});
		$("#EE336").attr({title: "Energy Systems", pre:"EE205 EE303 EE324"});
		$("#EE352").attr({title: "Intro to Electronics Lab", pre:"EE202 EE203", co:"EE310"});
		$("#EE353").attr({title: "Electronic Circuits Lab", pre:"EE352", co:"EE311"});
		$("#EE378").attr({title: "Digital Priciples", pre:"EE202", co:"EE310"});
		$("#EE379").attr({title: "Embedded Systems", pre:"EAS230 EE278 EE000"});
		$("#EE383").attr({title: "Communication Systems", pre:"EE205 EE305"});
		$("#EE408").attr({title: "Senior Seminar"});
		$("#EE409").attr({title: "Senior Design Implementation", pre:"EE408 EE311 EE436"});
		$("#EE410").attr({title: "Electronic Instrument Design I", pre:"EE310"});
		$("#EE436").attr({title: "Energy Systems", pre:"EE205 EE303 EE324"});
		$("#EE478").attr({title: "HDL Digital Design", pre:"EE278 EE379"});
		$("#EE494").attr({title: "Sr Design Impl", pre:""});
		
		// IE COURSES
		
		$("#IE101").attr({title: "Discover Industrial Engineering"});
		$("#IE306").attr({title: "Statistics for Engineers", pre:"EAS305"});
		$("#IE320").attr({title: "Engineering Economy"});
		$("#IE323").attr({title: "Ergonomics", co:"EAS305"});
		$("#IE326").attr({title: "Planning for Production"});
		$("#IE327").attr({title: "Facilities Design", pre:"IE326"});
		$("#IE373").attr({title: "Deterministric Models"});
		$("#IE374").attr({title: "Probabilistic Models", pre:"EAS305", co:"IE373"});
		$("#IE408").attr({title: "Quality Assurance", pre:"IE306"});
		$("#IE420").attr({title: "Systems Eng Practicum", co:"IE477", pre:"IE320 IE323 IE326 IE306 IE373 IE374"});
		$("#IE436").attr({title: "Work Physiology", pre:"IE323"});
		$("#IE477").attr({title: "Digital Simulation", pre:"IE306 IE374"});
		$("#IE496").attr({title: "Senior Capstone Internship", pre:"IE320 IE323 IE326 IE306 IE373 IE374"});
		
		$("#IE4XX").attr({pre:"IE323"});
		
		// MAE COURSES
		
		$("#MAE177").attr({title: "Engineering Drawing and CAD"});
		$("#MAE204").attr({title: "Thermodynamics I", pre: "MTH142"});
		$("#MAE277").attr({title: "Intro to Mechanical Engineering"/*, pre: "EAS140", co: "MAE177"*/});
		$("#MAE278").attr({title: "Intro to Aerospace Engineering"/*, pre: "EAS140"*/});
		$("#MAE311").attr({title: "Machines & Mechanisms I", pre: "EAS209", co: "MAE381"});
		$("#MAE315").attr({title: "Analysis of Structures", pre: "EAS209", co: "MAE376"});
		$("#MAE316").attr({title: "Aerospace Structures", pre: "MAE315"});
		$("#MAE334").attr({title: "MAE Laboratory I", pre: "EAS209 MAE340", co:"EE200"});
		$("#MAE335").attr({title: "Fluid Mechanics", pre: "EAS209"});
		$("#MAE336").attr({title: "Heat Transfer", pre: "MAE204"});
		$("#MAE338").attr({title: "MAE Lab II", pre: "MAE335 MAE336"});
		$("#MAE340").attr({title: "Dynamic Systems", pre: "EAS208", co: "MAE376"});
		$("#MAE345").attr({title: "Intermediate Dynamics", pre: "EAS208"});
		$("#MAE364").attr({title: "Manufacturing Processes", co: "MAE381"});
		$("#MAE376").attr({title: "Applied Math for MAE", pre: "EAS230 MTH306"});
		$("#MAE377").attr({title: "Product Design: CAE", pre: "MAE177", co: "EAS209"});
		$("#MAE381").attr({title: "Engineering Materials", pre: "CHE107"});
		$("#MAE385").attr({title: "Engineering Materials Lab", pre: "MAE381"});
		$("#MAE424").attr({title: "Aerodynamics", pre: "MAE335"});
		$("#MAE423").attr({title: "Intro to Propulsion", pre: "MAE335"});
		$("#MAE436").attr({title: "Flight Dynamics", pre: "EAS208 MAE340 MAE345 MAE424"});
		$("#MAE451").attr({title: "Design Process & Methods"});
		$("#MAE422").attr({title: "Gas Dynamics", pre: "MAE335"});
		$("#MAE425").attr({title: "Spacecraft Dynamics & Control", pre: "MAE345 MAE376"});
		$("#MAE434").attr({title: "Aircraft Design", pre: "MAE436"});
		$("#MAE494").attr({title: "Design Project", co: "MAE451"});
		
		// ESL FOR ITU FLOWSHEETS
		
		$("#ESL407").attr({title: "Written English I"});
		$("#ESL408").attr({title: "Written English II", pre:"ESL407"});
		
		
		// ITU PLACEHOLDERS
		$("#I-EAS207").attr({pre:"MTH141 PHY107",co:'MTH142'});
}