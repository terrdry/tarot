const validExtensions= ['png', 'jpg', 'jpeg', 'gif'] as const;
type ValidExtension = typeof validExtensions[number];

interface CardValidationRules {
    name: ((v: string) => boolean | string)[];
    img: ((v: string) => boolean | string)[];
}

const ERROR_MESSAGES = {
    NAME_REQUIRED: 'Name is required',
    NAME_LENGTH: 'Name must be less than 50 characters',
    NAME_FORMAT: 'Name can only contain letters, spaces, and hyphens',
    IMAGE_REQUIRED: 'Image is required',
    IMAGE_FORMAT: 'Image must be a valid format (PNG, JPG, JPEG, GIF)'
} as const;

export const isValidExtension = (filename: string): boolean => {
    console.log('filename', filename);
    const extension = filename.split('.').pop()?.toLowerCase();
    if (!extension)
        return false;
    return validExtensions.includes(extension as ValidExtension);
};

export const cardValidationRules: CardValidationRules = {
    name: [
        (v: string) => !!v || ERROR_MESSAGES.NAME_REQUIRED,
        (v: string) => v.length <= 50 || ERROR_MESSAGES.NAME_LENGTH,
        (v: string) => /^[a-zA-Z\s-]+$/.test(v) || ERROR_MESSAGES.NAME_FORMAT
    ],
    img: [
        (v: string) => !!v || ERROR_MESSAGES.IMAGE_REQUIRED,
        (v: string) => isValidExtension(v) || ERROR_MESSAGES.IMAGE_FORMAT,
    ]
};




export default cardValidationRules;
