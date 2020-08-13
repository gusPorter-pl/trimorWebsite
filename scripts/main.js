const changeDisplay = (thisSection) => {
   const allSections = ["home", "shop", "location", "news", "guestBook"];
   const otherSections = allSections.filter(section => section != thisSection);

   document.getElementById(thisSection).style.display = "block";
   document.getElementById(thisSection + "Tab").style.backgroundColor = "#a0a0a0";

   for (section of otherSections) {
      document.getElementById(section).style.display = "none";
      document.getElementById(section + "Tab").style.backgroundColor = "transparent";
   }
};

const search = () => {
   const textInput = document.getElementById("search").value;
   const contents = document.getElementById("contents");
   if (textInput === "") {
      contents.style.display = "block";
      // Show articles based off of textInput
   } else {
      contents.style.display = "none";
   }
}

window.onload = () => {
   document.getElementById("contents").style.display = "block";
}