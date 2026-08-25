import Svg, { ClipPath, Defs, G, Path, Rect } from "react-native-svg";
import { colors } from "../../theme/colors";

type Props = {
  size?: number;
  color?: string;
};

/** Figma icon 2016:187 — outer box 9.69 (scaled ×5/3 ≈ 16). */
export function ShareIcon({ size = 16, color = colors.text }: Props) {
  return (
    <Svg width={size} height={size} viewBox="0 0 9.69231 9.69231" fill="none">
      <G clipPath="url(#shareClip)">
        <Path
          d="M7.26923 3.23077C7.93834 3.23077 8.48077 2.68834 8.48077 2.01923C8.48077 1.35012 7.93834 0.807691 7.26923 0.807691C6.60012 0.807691 6.05769 1.35012 6.05769 2.01923C6.05769 2.68834 6.60012 3.23077 7.26923 3.23077Z"
          stroke={color}
          strokeWidth={0.807692}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <Path
          d="M2.42307 6.05769C3.09219 6.05769 3.63461 5.51527 3.63461 4.84615C3.63461 4.17704 3.09219 3.63461 2.42307 3.63461C1.75396 3.63461 1.21154 4.17704 1.21154 4.84615C1.21154 5.51527 1.75396 6.05769 2.42307 6.05769Z"
          stroke={color}
          strokeWidth={0.807692}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <Path
          d="M7.26923 8.88462C7.93834 8.88462 8.48077 8.34219 8.48077 7.67308C8.48077 7.00396 7.93834 6.46154 7.26923 6.46154C6.60012 6.46154 6.05769 7.00396 6.05769 7.67308C6.05769 8.34219 6.60012 8.88462 7.26923 8.88462Z"
          stroke={color}
          strokeWidth={0.807692}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <Path
          d="M3.46903 5.45597L6.2273 7.06327"
          stroke={color}
          strokeWidth={0.807692}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <Path
          d="M6.22326 2.62904L3.46903 4.23635"
          stroke={color}
          strokeWidth={0.807692}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </G>
      <Defs>
        <ClipPath id="shareClip">
          <Rect width={9.69231} height={9.69231} fill="white" />
        </ClipPath>
      </Defs>
    </Svg>
  );
}
