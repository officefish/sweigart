const readline = require("readline-sync")

const logger = require('./log_call_func')
const logStack = logger.logStack

const getRandomDate = (start, end) => {
  return new Date(
    start.getTime() + Math.random() * (end.getTime() - start.getTime())
  )
}

const getBirthdays = (numBirthdays) => {
  let birthdays = []
  let start = new Date(2000, 0, 0)
  let end = new Date(2000, 11, 30)
  for (let i = 0; i < numBirthdays; ++i)
    birthdays.push(getRandomDate(start, end))
  return birthdays
}
//console.log(getBirthdays(35).length)

const getMatch = (birthdays, options) => {
  let birthdaysSet = new Set()
  for (const birthday of birthdays.values()) {
    let size = birthdaysSet.size
    birthdaysSet.add(birthday.toLocaleDateString("en-US", options))
    if (size === birthdaysSet.size) return birthday
  }
  return null
}
//console.log(getMatch(getBirthdays(35)))

const getInputNumBirthdays = () => {
  while (true) {
    answer = readline.question(
      "\nHow many Birthdays shall I generate? (Max 100): "
    )
    if (!isNaN(answer) && 0 < +answer <= 100) return +answer
  }
}

const printIntro = () => {
  const intro = `\nBirthday Paradox, by A. Sweigart.
    ...`
  console.log(intro)
  logStack()
}

const printBirthdays = (numBirthdays, options) => {
  let output = `\nHere are ${numBirthdays} birthdays: `
  for (const [index, birthday] of numBirthdays.entries()) {
    if (index) output += ", "
    output += birthday.toLocaleDateString("en-US", options)
  }
  console.log(output)
}

const printMatch = (match, options) => {
  let output = "\n\nIn this simulation, "
  output += match
    ? `multiply people have a birthday on ${match.toLocaleDateString(
        "en-US",
        options
      )}.`
    : "there are no matching birthdays."
  output += "\n"
  console.log(output)
}

const printGenerationIntro = (numBirthdays) => {
  console.log(`\nGenerating ${numBirthdays} random birthdays 100,000 times...`)
}

const getInputEnterAgreement = () => {
  readline.question('\nPress "Enter" to start generation')
}

const runGeneration = (numBirthdays, numSimulations) => {
  if (numSimulations > 100_000 || numSimulations < 1)
    throw new TypeError(`${numSimulations} is too much for pet project. Sorry!`)

  let simMatch = 0
  const nunSimulationsFraction = Math.round(numSimulations / 10)
  for (let i = 0; i < numSimulations; ++i) {
    if (!(i % nunSimulationsFraction)) console.log(`${i} simulations run`)
    const birthdays = getBirthdays(numBirthdays)
    if (getMatch(birthdays)) ++simMatch
  }
  console.log(`${numSimulations} simulations run.`)
  return simMatch
}

const getProbability = (simMatch, simNum) => {
  return Math.round((simMatch / simNum) * 100) / 100
}

const printConclusion = (
  numSimulations,
  numBirthdays,
  simMatch,
  probability
) => {
  console.log(
    `\nOut of ${numSimulations} simulations of ${numBirthdays} people, there was a`
  )
  console.log(`mathcing birthday in that group ${simMatch} times. That means`)
  console.log(`that ${numBirthdays} people have a ${probability} % chance of`)
  console.log(
    `having a mathcing birthday in their group.\nThat\'s probably more than you would think!\n`
  )
}

const main = () => {
  printIntro()
  const numBirthdays = getInputNumBirthdays()
  const birthdays = getBirthdays(numBirthdays)
  const dateOptions = { month: "short", day: "numeric" }
  printBirthdays(birthdays, dateOptions)

  const match = getMatch(birthdays, dateOptions)
  printMatch(match, dateOptions)
  printGenerationIntro(numBirthdays)
  getInputEnterAgreement()
  const numSimulations = 100_000
  const simMatch = runGeneration(numBirthdays, numSimulations)
  const probability = getProbability(simMatch, numSimulations)
  printConclusion(numSimulations, numBirthdays, simMatch, probability)
}

main()
