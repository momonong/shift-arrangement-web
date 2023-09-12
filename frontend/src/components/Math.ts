export const calculate_get = async (operator: string, a: number, b: number) => {
  const params = new URLSearchParams({operator, a: a.toString(), b: b.toString()});
  const response = await fetch(`http://127.0.0.1:8000/math_get?${params.toString()}`);
  const {result} = await response.json();
  return result;
};

const calculate_post = async () => {
  const response = await fetch('http://127.0.0.1:8000/math_post',{
    method: 'POST', 
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({operator: 'add', a: 1, b: 2}),
  });
  const {result} = await response.json();
  console.log(result);
}
calculate_post();