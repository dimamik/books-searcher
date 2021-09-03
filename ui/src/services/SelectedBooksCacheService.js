import axios from "axios";

const API_PATH = "http://185.46.11.241:5001";

export const deleteSelectedBook = (newListOfBooks, bookToRemove) => {
    // window.localStorage.setItem('selectedBooks', JSON.stringify(newListOfBooks));
    let user_id = window.localStorage.getItem("user_id");

    if (user_id) {
        axios
            .delete(
                `${API_PATH}/record/?user_id=${user_id}&book_id=${bookToRemove.book_id}`
            )
            .then();
    }
};
