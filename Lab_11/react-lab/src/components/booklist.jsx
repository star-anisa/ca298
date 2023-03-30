import { useState, useEffect } from "react";

function BookList() {
  const [books, setBooks] = useState([]);
  const displayFacts = () => {
    return books.map(element => <div><li>{element.title} </li><hr /></div>);
  };
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/book/")
      .then(response => response.json())
      .then(data => {
        setBooks(data.map(element => element))
        setIsLoaded(true);
		console.log(data)
      })
      .catch(error => console.log(error));
  }, [])
  if (isLoaded) {
    return (
      <div>
        <h1>Library</h1> 
      <ul>
        {displayFacts()}
      </ul></div>
    )
  }
  return (
    <p>Data is loading. Please stand by. Beep Boop</p>
  )
}

export default BookList;
