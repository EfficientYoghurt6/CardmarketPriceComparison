import React from 'react'
import ExpansionSelector from './components/ExpansionSelector'
import CardList from './components/CardList'
import EVCalculator from './components/EVCalculator'
import ApiKeyForm from './components/ApiKeyForm'

const App: React.FC = () => {
  return (
    <div className="app-container">
      <h1>Cardmarket Price Comparison</h1>
      {/* Placeholder components */}
      <ApiKeyForm />
      <ExpansionSelector />
      <CardList />
      <EVCalculator />
    </div>
  )
}

export default App
