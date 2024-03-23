import { useEffect, useState } from 'react'
import './App.css'

interface Host {
  name: string
}

const baseUrl = 'http://localhost:8001'

function App() {
  const [hosts, setHosts] = useState<Host[]>([])
  const [targets, setTargets] = useState<string>()

  const loadHosts = async () => {
    const hosts = await fetch(`${baseUrl}/hosts/`)
    setHosts(await hosts.json())
  }

  useEffect(() => {
    loadHosts()
  }, [])

  const getTargets = async () => {
    const targets = await fetch(`${baseUrl}/targets/`)
    const result = await targets.json()
    console.log(result)
    setTargets(JSON.stringify(result, null, 2))
  }

  return (
    <>
      <div className="card">
        <h2>Hosts</h2>
        { hosts.map((h, i) => {
            return (
              <div key={ i }>{ h.name }</div>
            )
        }) }
      </div>
      <div>
        <button onClick={ getTargets }>Refresh Targets</button>
        <pre>
          { targets }
        </pre>
      </div>
    </>
  )
}

export default App
