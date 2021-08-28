import {ThemeProvider} from "styled-components";
import {darkTheme, lightTheme} from "./components/Theme/Themes";
import {useDarkMode} from "./components/Theme/UseDarkMode";
import ThemeToggler from "./components/Theme/Toggler";
import {GlobalStyles} from "./components/GlobalStyles";
import ReactFullpage from '@fullpage/react-fullpage';
import React, {useState} from "react";
import WelcomePage from "./components/WelcomePage/WelcomePage";
import ChooseBookDialog from "./components/ChooseBook/ChooseBookDialog";
import SelectedBooks from "./components/SelectedBooks/SelectedBooks";
import {CssBaseline} from "@material-ui/core";
import SearchPage from "./components/SearchPage/SearchPage";
import Recommendations from "./components/Recommendations/Recommendations";


// Context to be able to select book from each react component being the child of
// selectBookContext.Provider
export const selectBookContext = React.createContext("");

function App() {

    const [theme, switchTheme] = useDarkMode();

    const [bookSelectedDialogState, setBookSelectedDialogState] = React.useState(false);

    const [selectedBook, setSelectedBook] = useState("");

    let [booksReadList, setBooksReadList] = useState([]);

    const themeMode = theme === 'light' ? lightTheme : darkTheme;


    let booksReadProvider = [booksReadList, setBooksReadList]

    const anchors = ["welcomePage", "searchPage", "managePage", "recPage"];


    const selectBook = (book) => {
        setSelectedBook(book);
        setBookSelectedDialogState(true);
    }
    const bookSelectedAction = (book) => {
        // saveSelectedBooks([...booksReadList, book]);

        setBooksReadList([...booksReadList, book]);

        setBooksReadList(booksReadList.filter((thing, index, self) =>
                index === self.findIndex((t) => (
                    t._id === thing._id
                ))
        ));

    }
    //TODO Play with ReactFullPage more
    // normalScrollElements are elements that can normally scroll nevertheless ReactFullPage blocking the scroll
    return (

        <ThemeProvider theme={themeMode}>

            <GlobalStyles/>
            {/*Using normalize.css normalize the stylesheet*/}
            <CssBaseline/>

            <selectBookContext.Provider value={selectBook}>

                <ThemeToggler switchTheme={switchTheme}/>

                <ChooseBookDialog open={bookSelectedDialogState} setOpen={setBookSelectedDialogState}
                                  selectedBook={selectedBook}
                                  bookSelectedAction={bookSelectedAction}
                />
                <ReactFullpage
                    normalScrollElements={`.scrollable-content`}
                    debug
                    anchors={anchors}
                    navigation
                    slidesNavigation
                    // navigationTooltips={anchors}
                    onLeave={(origin, destination, direction) => {
                        console.log("onLeave event", {origin, destination, direction});
                    }}
                    render={({state, fullpageApi}) => {
                        console.log("render prop change", state, fullpageApi); // eslint-disable-line no-console

                        return <div>
                            <WelcomePage/>
                            <SearchPage/>
                            <SelectedBooks booksReadProvider={booksReadProvider}/>
                            <Recommendations userPreference={booksReadList}/>
                        </div>

                    }}

                />
            </selectBookContext.Provider>
        </ThemeProvider>

    );
}

export default App;
