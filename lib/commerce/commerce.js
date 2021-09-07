import Commerce from "@chec/commerce.js";

const checPK = process.env.SANDBOX_PUBLIC_KEY;
const devEnv = process.env.NODE_ENV === 'development';

if (devEnv && !checPK){
    throw Error("just provide a public key")
}

export const commerce = new Commerce(checPK, devEnv)