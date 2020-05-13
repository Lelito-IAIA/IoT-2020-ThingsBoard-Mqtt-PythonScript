
    var isMobile = navigator.userAgent.match(/(iPhone|iPod|iPad|Android)/); 
    let movement = 0;
    let isMoving = false
    //if the user is using a mobile it will have the Accelerometer sensor
    if (isMobile != null) {
      document.getElementById("qr").style.display = 'none';
      //LinearAccelerationSensor is subclass of Accelerometer, and measures acceleration applied to 
      //the device excluding the acceleration contributed by gravity. It uses x, y, and z properties as above.
      let sensor = new LinearAccelerationSensor({frequency: 1});
      //starting the sensor
      sensor.start();
      //on reading function

      function setStatus(status) {
        document.getElementById("result").textContent = status
      }

      sensor.onreading = () => {
        let x = sensor.x
        let y = sensor.y
        let z = sensor.z
        //sending the data to the html table
        document.getElementById("motionX").textContent = x
        document.getElementById("motionY").textContent = y
        document.getElementById("motionZ").textContent = z
        
        //calculating the length of the acceleration vector
        movement = Math.sqrt(x*x + y*y + z*z);
        
        
        //sending the movement status to html row "motionOverall" of the table
        document.getElementById("motionOveral").textContent = movement.toFixed(2)

        //If the vector is less then a threshold (i.e. 0.6) the user is sitting or standing
        //instead if the vector length is more then a threshold the user is **walking** 
        document.getElementById("motionOveral").textContent = movement.toFixed(2)

        if (movement > 0.6) {
          setStatus("Walking")
          isMoving = true
        } else {
          setStatus("Sitting or standing")
          isMoving = false
        }

        console.log("Acceleration along X-axis: " + sensor.x);
        console.log("Acceleration along Y-axis: " + sensor.y);
        console.log("Acceleration along Z-axis: " + sensor.z);

        //sending data to thingsboard
        const Http = new XMLHttpRequest();
        //Cloud device link
        const url='https://demo.thingsboard.io/api/v1/prKQ09PTQM2Zd42OAoIt/telemetry';
        //Edge device link
        const url1='https://demo.thingsboard.io/api/v1/QflHryz6igJ5cLzHpYiy/telemetry';
        Http.open("POST",url);
        Http.send('{\"X\":\" ' + sensor.x +'\", \"Y\":'+ sensor.y +', \"Z\": '+ sensor.z + '}');
        Http.open("POST",url1);
        Http.send('{\"X\":\" ' + sensor.x +'\", \"Y\":'+ sensor.y +', \"Z\": '+ sensor.z + ', \"Moving\": '+ isMoving + '}');
      }
      setInterval(updateStatus, 100)
    } else {
      //if the WebApp is open on a desktop, you cannot use it!
      setStatus("Please open this site on your smartphone")
      //then a qrcode is shown leading to the webapp
      document.getElementById("qr").style.display = 'block';
      document.getElementById("chances").style.display = 'none';
    }
sensor.onerror = event => console.log(event.error.name, event.error.message);
