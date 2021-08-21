import axios from "axios";

export const serviceSearchAPI = (query) => {
    return new Promise(
        ((resolve, reject) => {
                axios.get(`http://localhost:5000/search/${query}`)
                    .then((response) => {
                        resolve(response.data.hits.hits);
                    })
            }
        )
    )
}
export const serviceSearchAsYouType = (query) => {
    return new Promise(
        ((resolve, reject) => {
                axios.get(`http://localhost:5000/saut/${query}`)
                    .then((response) => {
                        resolve(response.data.hits.hits);
                    }).catch(
                    (err) => reject("Problem with server: " + err)
                )
            }
        )
    )
}