import axios from "axios";
import {REC_API} from "./HostConfig";

let API_PATH = REC_API;

export const deleteSelectedBook = (newListOfBooks, bookToRemove) => {
    // window.localStorage.setItem('selectedBooks', JSON.stringify(newListOfBooks));
    let user_id = window.localStorage.getItem("user_id");
    console.log(bookToRemove);
    if (user_id) {
        axios
            .delete(
                `${API_PATH}/record/?user_id=${user_id}&book_id=${bookToRemove._id}`
            )
            .then();
    }
};

export const deleteCachedUserId = () => {
    window.localStorage.removeItem("user_id");

}