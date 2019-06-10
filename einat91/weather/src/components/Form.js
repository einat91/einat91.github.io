import React from "react";

const Form = props => (
	<form onSubmit={props.getWeather}>
		<input type="text" name="city" placeholder="enter a city"/>
		<button>Get Weather</button>
	</form>
);

export default Form;