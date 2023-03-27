import { useState, useEffect } from "react";

function CatFacts() {
	const [facts, setFacts] = useState(["cats are cool", "cats are nice"]);
	const [isLoaded, setIsLoaded] = useState(false);

	useEffect(()=>{
		// our code goes here 
		fetch("https://cat-fact.herokuapp.com/facts")
		.then(response=>response.json())
		.then(data=>{
			setFacts(data.map(e=>e.text)) // get the array of text out and set it as our state
			setIsLoaded(true);
		})
		.catch(err=>console.log(err))
	})
	const displayFacts = () =>{
		return facts.map(elem=>
			<li>{elem}</li> // return the jsx to render
		)
	}

	if(isLoaded){
        return (
            <ul>
                {displayFacts()}
            </ul>
        )
    }
    else{
        return (
            <img src="loading.gif" />
        )
    }
}

export default CatFacts;