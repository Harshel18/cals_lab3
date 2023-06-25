document.getElementById("harshel_list").addEventListener("click", function(e) {
    const adv = ["squt","pwd","sin","cos","tan"]
    if (e.target.id == "clear")
      {
        result.value = ""
      }
    else if (e.target.id == "cal" )
      {
        result.value = result.value.replace(/squt/g,'Math.sqrt',)
        result.value = result.value.replace(/pow/g,'Math.pow',)
        result.value = result.value.replace(/sin/g,'Math.sin',)
        result.value = result.value.replace(/cos/g,'Math.cos',)
        result.value = result.value.replace(/tan/g,'Math.tan',)

        return result.value = eval(result.value)
      }
    adv.includes(e.target.id) ? result.value= e.target.id + "("+result.value +")": result.value+=e.target.value
  });