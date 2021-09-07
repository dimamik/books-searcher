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
import {getRecommendations, getUserFavourite} from "./services/RecomService";


// Context to be able to select book from each react component being the child of
// selectBookContext.Provider
export const selectBookContext = React.createContext("");

function App() {

    const [theme, switchTheme] = useDarkMode();

    // ChooseBookDialog
    const [chooseBookDialogState, setChooseBookDialogState] = useState(false);

    // Book Selected to pass to chooseBookDialog
    const [selectedBook, setSelectedBook] = useState("");

    let [booksReadList, setBooksReadList] = useState([]);

    let [recommendationsList, setRecommendationsList] = useState([]);

    let [isBookSelected, setIsBookSelected] = useState(0);


    let recProvider = [recommendationsList, setRecommendationsList];


    let booksReadProvider = [booksReadList, setBooksReadList]


    const themeMode = theme === 'light' ? lightTheme : darkTheme;

    const anchors = ["welcomePage", "searchPage", "managePage", "recPage"];


    const selectBook = (book) => {
        setSelectedBook(book);
        setChooseBookDialogState(true);
    }

    const bookSelectedAction = (book) => {

        setBooksReadList([...booksReadList, book]);

        setBooksReadList(booksReadList.filter((thing, index, self) =>
                index === self.findIndex((t) => (
                    t._id === thing._id
                ))
        ));

        setIsBookSelected(isBookSelected + 1);

    }


    return (

        <ThemeProvider theme={themeMode}>

            <GlobalStyles/>
            {/*CssBaseline is using normalize.css to normalize the stylesheet*/}
            <CssBaseline/>

            <selectBookContext.Provider value={selectBook}>

                <ThemeToggler
                    switchTheme={switchTheme}/>

                <ChooseBookDialog
                    open={chooseBookDialogState}
                    setOpen={setChooseBookDialogState}
                    selectedBook={selectedBook}
                    bookSelectedAction={bookSelectedAction}
                />
                <ReactFullpage
                    normalScrollElements={`.scrollable-content`}
                    anchors={anchors}
                    navigation
                    slidesNavigation
                    onLeave={(origin, destination, direction) => {
                        // console.log("onLeave event", {origin, destination, direction});

                        //    Setting selected books
                        if (destination.anchor === 'managePage') {
                            getUserFavourite().then(
                                (result) => {
                                    if (result == null) {
                                        setBooksReadList([]);
                                    } else {
                                        setBooksReadList(result.data);
                                    }
                                }
                            )
                        }
                        //Setting recommendations
                        if (destination.anchor === 'recPage') {
                            getRecommendations().then((result) => {
                                if (result != null) {
                                    setRecommendationsList(result.data);
                                } else {
                                    setRecommendationsList([]);
                                }
                            })
                        }
                    }}
                    render={({state, fullpageApi}) => {
                        // console.log("render prop change", state, fullpageApi); // eslint-disable-line no-console

                        return <div>
                            <WelcomePage/>
                            <SearchPage isBookSelected={isBookSelected}/>
                            <SelectedBooks booksReadProvider={booksReadProvider}/>
                            <Recommendations recProvider={recProvider}/>
                        </div>

                    }}

                />
            </selectBookContext.Provider>
        </ThemeProvider>

    );
}

export default App;
