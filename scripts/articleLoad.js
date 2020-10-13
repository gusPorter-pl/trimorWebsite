const getArticles = () => {
   const path = window.location.pathname;
   const page = path.split("/");
   const articleType = page[2];
   const div = document.getElementById(articleType);
   fetch("../json/articles.json")
   .then((response) => response.json())
   .then(articlesObject => {
      const articles = articlesObject[articleType];
      articles.forEach((article) => {
         const fileLocation = "./" + article + ".html";
         article = capitalise(article);

         const header = document.createElement("h3");
         const anchor = document.createElement("a");
         anchor.href = fileLocation;
         anchor.innerHTML = article;
         
         header.appendChild(anchor);
         div.appendChild(header);
      });
   });
}

const capitalise = aString => {
   aString = aString.charAt(0).toUpperCase() + aString.slice(1, aString.length);
   for (let i = 0; i < aString.length; i++) {
      if (aString.charAt(i) == "-") {
         aString = aString.slice(0, i) + " " + aString.charAt(i + 1).toUpperCase() + aString.slice(i + 2, aString.length);
      }
   } return aString;
};

window.onload = () => {
   getArticles();
}