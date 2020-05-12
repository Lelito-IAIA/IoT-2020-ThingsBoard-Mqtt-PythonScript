
  function testDeviceOrientation() {
    if (typeof DeviceOrientationEvent !== 'function') {
      return setResult('DeviceOrientationEvent not detected')
    }
    if (typeof DeviceOrientationEvent.requestPermission !== 'function') {
      return setResult('DeviceOrientationEvent.requestPermission not detected')
    }
    DeviceOrientationEvent.requestPermission().then(function(result) {
      return setResult(result);
    });
  }
    
    function setStatus(status) {
      document.getElementById("result").textContent = status
    }
  
  
  
    var isMobile = navigator.userAgent.match(/(iPhone|iPod|iPad|Android)/); 
    let movement = 0;
    let isMoving = false
    if (isMobile != null) {
      let sensor = new LinearAccelerationSensor({frequency: 1});
      sensor.start();

      setTimeout(function() {
        document.getElementById("body").style.display = 'block'
      }, 1000)

      sensor.onreading = () => {
        let x = sensor.x
        let y = sensor.y
        let z = sensor.z
        document.getElementById("motionX").textContent = x
        document.getElementById("motionY").textContent = y
        document.getElementById("motionZ").textContent = z
        
       
        movement = Math.sqrt(x*x + y*y + z*z);
        
        

        document.getElementById("motionOveral").textContent = movement.toFixed(2)
        if (movement > 0.5) {
          setStatus("Walking")
          isMoving = true
        } else {
          setStatus("Sitting or standing")
          isMoving = false
        }

        console.log("Acceleration along X-axis: " + sensor.x);
        console.log("Acceleration along Y-axis: " + sensor.y);
        console.log("Acceleration along Z-axis: " + sensor.z);
        const Http = new XMLHttpRequest();
        const url='https://demo.thingsboard.io/api/v1/prKQ09PTQM2Zd42OAoIt/telemetry';
        const url1='https://demo.thingsboard.io/api/v1/QflHryz6igJ5cLzHpYiy/telemetry';
        Http.open("POST",url);
        Http.send('{\"X\":\" ' + sensor.x +'\", \"Y\":'+ sensor.y +', \"Z\": '+ sensor.z + '}');
        Http.open("POST",url1);
        Http.send('{\"X\":\" ' + sensor.x +'\", \"Y\":'+ sensor.y +', \"Z\": '+ sensor.z + ', \"Moving\": '+ isMoving + '}');
        document.getElementById("payload").textContent = payload
      }
      setInterval(updateStatus, 100)
    } else {
      setStatus("Please open this site on your smartphone")
      document.getElementById("qr").style.display = 'block';
      document.getElementById("chances").style.display = 'none';
    }
sensor.onerror = event => console.log(event.error.name, event.error.message);