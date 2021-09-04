import axios from "axios";
import {SEARCH_API} from "./HostConfig";

let API_PATH = SEARCH_API;

export const serviceSearchAPI = (query) => {
    return new Promise(
        ((resolve, reject) => {
                axios.get(`${API_PATH}/search/${query}`).then((response) => {
                    resolve(response.data.hits.hits);
                });
            }
        )
    )
}
export const serviceSearchAsYouType = (query) => {
    return new Promise(
        ((resolve, reject) => {
                axios
                    .get(`${API_PATH}/saut/${query}`)
                    .then((response) => {
                        resolve(response.data.hits.hits);
                    })
                    .catch((err) => reject("Problem with server: " + err));
            }
        )
    )
}

export const searchBookInGoogle = (book_name) => {
    let search_query = book_name + " fb2"
    window.open('https://google.com/search?q=' + search_query);

}
