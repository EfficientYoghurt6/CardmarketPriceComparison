import React, { useState } from 'react'

interface ApiKeyFormProps {}

const ApiKeyForm: React.FC<ApiKeyFormProps> = () => {
  const [key, setKey] = useState('')

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    await fetch('http://localhost:8100/apikey', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ api_key: key })
    })
    setKey('')
  }

  return (
    <form onSubmit={submit}>
      <input
        type="password"
        value={key}
        onChange={(e) => setKey(e.target.value)}
        placeholder="Cardmarket API key"
      />
      <button type="submit">Save</button>
    </form>
  )
}

export default ApiKeyForm
