import axios from "axios";

export const addBookToFav = (book_id) => {
    let user_id = window.localStorage.getItem('user_id');
    if (!user_id) {
        return new Promise((resolve) => axios.get(`http://localhost:5001/get_user_number`)
            .then((response) => {
                window.localStorage.setItem('user_id', response.data);
                return response.data;
            }).then(
                (user_id) => axios.get(`http://localhost:5001/record/?user_id=${user_id}&book_id=${book_id}`).then(resolve)
            ))

    } else {
        return new Promise((resolve) =>
            axios.get(`http://localhost:5001/record/?user_id=${user_id}&book_id=${book_id}`).then(resolve)
        )
    }

}


export const getRecommendations = () => {
    let user_id = window.localStorage.getItem('user_id');
    console.log(user_id);
    if (!user_id) {
        return new Promise((resolve) => resolve(null));
    } else {
        return new Promise((resolve) =>
            axios.get(`http://localhost:5001/recommend/?user_id=${user_id}`).then((result) =>
                resolve(result)
            )
        )
    }
}

export const getUserFavourite = () => {
    let user_id = window.localStorage.getItem('user_id');
    if (!user_id) {
        return new Promise((resolve) => resolve(null));
    } else {
        return new Promise((resolve) =>
            axios.get(`http://localhost:5001/get_user_favourite/?user_id=${user_id}`).then((result) =>
                resolve(result)
            )
        )
    }
}