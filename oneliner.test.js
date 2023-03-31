const oneliner = require('./oneliner.js')

describe('Shuffle oneliner', () => {
  
  test('shuffle with random length should be same length after shuffle' , () => {
    const random = Math.trunc(Math.random() * 100)
    expect( oneliner.shuffle(Array(random)).length ).toBe(random)
  })

  /*
  test('shuffled Array should includes all same values', () => {
    const random = Math.trunc(Math.random() * 100)
    const randomArray = Array(random)
    const randomElement = randomArray[Math.floor(Math.random() * randomArray.length)]
    expect(_s.shuffle(randomArray.includes(randomElement))).toBe(true)
  })

  test('shuffled Array should be well shuffles', () => {
    const random = Math.trunc(Math.random() * 100)
    const randomArray = Array(random)
    const shaffledArray = _s.shuffle(randomArray)
    let same = true
    for (const key of randomArray.keys()) {
      if (randomArray[key]!== shaffledArray[key]) {
        same = false
        break
      }
    }      
   expect(same).not.toEqual(true)
  // expect(_s.shuffle([0,1,2,3,4])).contains(0)
  })
  */
})

