import axios from "axios";

// export const saveSelectedBooks = (booksList) => {
// //    TODO Check if cache is empty
//     let selectedPrevBooks = loadSelectedBooks();
//     let cachedBooks = booksList.concat(selectedPrevBooks);
//
// //    if cache is not empty, than write only unique values
//
//     cachedBooks = cachedBooks.filter((thing, index, self) =>
//             index === self.findIndex((t) => (
//                 t._id === thing._id
//             ))
//     )
//
//
//     window.localStorage.setItem('selectedBooks', JSON.stringify(cachedBooks));
//
//     return cachedBooks;
// }
//
// export const loadSelectedBooks = () => {
//
//     let to_ret = window.localStorage.getItem('selectedBooks');
//
//     if (to_ret == null) {
//         return [];
//     }
//
//     to_ret = JSON.parse(to_ret);
//
//     to_ret = to_ret.filter((thing, index, self) =>
//             index === self.findIndex((t) => (
//                 t._id === thing._id
//             ))
//     )
//
//     return to_ret;
//
// }

export const deleteSelectedBook = (newListOfBooks, bookToRemove) => {

    // window.localStorage.setItem('selectedBooks', JSON.stringify(newListOfBooks));
    let user_id = window.localStorage.getItem('user_id');

    if (user_id) {
        axios.delete(`http://localhost:5001/record/?user_id=${user_id}&book_id=${bookToRemove.book_id}`).then();
    }
}

