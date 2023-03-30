import { useState, useEffect } from "react";

function Singlebook({ number }) {
  const [books, setBooks] = useState([]);
  const [isLoaded, setIsLoaded] = useState(false);
  const num = parseInt(number);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/book/${num}/`)
      .then(response => response.json())
      .then(data => {
        setBooks([data]);
        setIsLoaded(true);
      })
      .catch(err => console.log(err))
  }, [num]);

  const displayFacts = () => {
    return books.map(element => (
      <li>{element.title} By: {element.author}<br />Released on: {element.year} of Genre {element.genre}</li>
    ));
  };

  if (isLoaded) {
    return <div> <h1>Book details</h1><ul>{displayFacts()}</ul> </div>;
  } else {
    return <p>Data is loading. Please stand by. Beep Boop</p>;
  }
}

export default Singlebook;
