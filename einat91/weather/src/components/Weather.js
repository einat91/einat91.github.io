import React from "react";

const Weather = props => (
	<div className="weather__info">
		{
			props.city && props.country && props.icon && <p className="location">
				<span className="weather__value"> {props.city}, {props.country}</span>
				<img className="weatherIcon" src={`https://openweathermap.org/img/w/${props.icon}.png`} alt="icon" />
			</p>
		}
		{
			props.temperature && <p className="weather__key"> Temperature:
	 		<span className="weather__value"> {props.temperature}	</span>
			</p>
		}
		{
			props.description && <p className="weather__key"> Conditions:
	 		<span className="weather__value"> {props.description} </span>
			</p>
		}
		{
			props.humidity && <p className="weather__key"> Humidity:
	 		<span className="weather__value"> {props.humidity} </span>
			</p>
		}
		{
			props.windspeed && <p className="weather__key"> Wind Speed:
	 		<span className="weather__value"> {props.windspeed} </span>
			</p>
		}
		{
			props.error && <p className="weather__error">{props.error}</p>
		}
	</div>
);

export default Weather;