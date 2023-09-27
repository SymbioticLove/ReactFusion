
import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './redux/store';

import { useSelector } from 'react-redux';

const HomePage = () => {
  const homePageData = useSelector(state => state.about.homepage);
  return (
    <div>
      <h1>{homePageData.welcome}</h1>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Router>
          <Routes>
            <Route exact path="/" element={<HomePage />} />
            <Route path="/route1" />
            <Route path="/route2" />
            <Route path="/route3" />
          </Routes>
        </Router>
      </Provider>
    </div>
  );
}

export default App;
