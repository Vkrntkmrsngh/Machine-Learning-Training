$(document).ready(function(){
  
  //On submitting the Predit button below code will be processed
  $("#submit").on("click",function(){
	
	//Fetch all the input fields value
	var creditscore = $.trim($("#creditscore").val());
	var geography = $.trim($("#geography").val());
	var gender = $.trim($("#gender").val());
	var age = $.trim($("#age").val());
	var tenure = $.trim($("#tenure").val());
	var balance = $.trim($("#balance").val());
	var hascrcard = $.trim($("#hascrcard").val());
	var isactivemember = $.trim($("#isactivemember").val());
	var estimatedsalary = $.trim($("#estimatedsalary").val());
	  
	
	if(creditscore == "" || geography == "" || gender == "" || age == "" || tenure == "" || balance == "" || hascrcard == "" || isactivemember == "" || estimatedsalary =="")
	{
      
	  // you may allow it as per your model needs
      // you may mark some fields with * (star) and make sure they aren't empty here
		alert("empty fields not allowed");
    
	
	}
    else{
      
	  
	  // replace <username> with your pythonanywhere username
      // also make sure to make changes in the url as per your flask API argument names
      var requestURL = "http://127.0.0.1:5000/cuspredict/?creditscore="+creditscore+"&geography="+geography+"&gender="+gender+"&age="+age+"&tenure="+tenure+"&balance="+balance+"&hascrcard="+hascrcard+"&isactivemember="+isactivemember+"&estimatedsalary="+estimatedsalary;
      //alert(requestURL); // log the requestURL for troubleshooting
      //debugger
	 
	 /*
	  $.getJSON(requestURL, function(data) {
        console.log(data); // log the data for troubleshooting
        //prediction = data['json_key_for_the_prediction'];
		alert(data);
      });
      */
	  
	  
	  var xhr = new XMLHttpRequest();
	  
	 // alert(xhr.readyState);
	  
	  xhr.open("GET",requestURL,true);
	  
	 // alert(xhr.readyState);
	  
	  xhr.onload = function(){
		  
		  if(xhr.status == 200){
			  if(xhr.responseText == 1)
			  {
				  $(".result").html("Prediction is:Yes");
			  }
			  else
			  {
				  $(".result").html("Prediction is:No");
			  }
		  }
			
	  };
	  
	  xhr.send();
	  return false;
	  
	  // following lines consist of action that would be taken after the request has been read
      // for now i am just changing a <h2> tag's inner html using jquery
      // you may simple do: alert(prediction);
      //$(".result").html("Prediction is:" + prediction);
    }
	  
	  
  });
  
  
  
});
